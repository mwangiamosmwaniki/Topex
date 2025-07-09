from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from academics.models import Message, Unit, LectureNote, Timetable, Assignment, Submission
from lecturers.models import LecturerProfile
from .forms import LectureNoteForm, AssignmentForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist


def lecturer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            try:
                lecturer_profile = user.lecturerprofile
                login(request, user)
                return redirect('core:lecturer_dashboard')
            except ObjectDoesNotExist:
                messages.error(request, "Lecturer profile not found for this account.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'lecturers/login.html')

def lecturer_logout(request):
    logout(request)
    return redirect('lecturers:login')

@login_required
def dashboard(request):
    lecturer = request.user.lecturerprofile
    units = Unit.objects.filter(lecturer=request.user)

    # Get all assignments linked to this lecturer's units
    assignments = Assignment.objects.filter(unit__in=units)

    # Get recent submissions for those assignments
    submissions = Submission.objects.filter(assignment__in=assignments).select_related('student', 'assignment').order_by('-submitted_at')[:10]

    context = {
        'lecturer': lecturer,
        'units': units,
        'assignments': assignments,
        'submissions': submissions,
        'courses_count': units.count(),
        'assignments_count': assignments.count(),
        'submissions_count': Submission.objects.filter(assignment__in=assignments).count(),
    }
    return render(request, 'lecturers/dashboard.html', context)


@login_required
def unit_detail(request, unit_id):
    lecturer = request.user.lecturerprofile
    unit = get_object_or_404(Unit, id=unit_id, lecturer=request.user)
    notes = unit.notes.all().order_by('week')
    return render(request, 'lecturers/unit_detail.html', {'unit': unit, 'notes': notes})

@login_required
def upload_materials(request):
    lecturer = request.user.lecturerprofile
    units = Unit.objects.filter(lecturer=request.user)

    if request.method == 'POST':
        form = LectureNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user  # uploaded_by is a User
            note.save()
            return redirect('lecturers:upload_materials')
    else:
        form = LectureNoteForm()

    notes = LectureNote.objects.filter(uploaded_by=request.user).order_by('week', 'unit__code')
    notes_by_week = defaultdict(list)
    for note in notes:
        notes_by_week[note.week].append(note)

    return render(request, 'lecturers/upload_materials.html', {
        'form': form,
        'units': units,
        'materials_by_week': dict(notes_by_week),
    })

@login_required
def edit_note(request, pk):
    lecturer = request.user.lecturerprofile
    note = get_object_or_404(LectureNote, pk=pk, uploaded_by=request.user)
    if request.method == 'POST':
        form = LectureNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('lecturers:upload_materials')
    else:
        form = LectureNoteForm(instance=note)

    return render(request, 'lecturers/edit_note.html', {'form': form})

@login_required
def delete_note(request, pk):
    lecturer = request.user.lecturerprofile
    note = get_object_or_404(LectureNote, pk=pk, uploaded_by=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('lecturers:upload_materials')
    return render(request, 'lecturers/confirm_delete.html', {'note': note})

@login_required
def assigned_units(request):
    lecturer = request.user.lecturerprofile
    units = Unit.objects.filter(lecturer=request.user)  # fixed
    return render(request, 'lecturers/assigned_units.html', {'lecturer': lecturer, 'units': units})

@login_required
def Messages(request):
    lecturer = request.user.lecturerprofile
    messages_list = Message.objects.filter(recipient=request.user).order_by('-timestamp')  # use User
    return render(request, 'lecturers/messages.html', {'lecturer': lecturer, 'messages': messages_list})

@login_required
def timetables(request):
    lecturer = request.user.lecturerprofile
    timetables = Timetable.objects.filter(lecturer=lecturer)
    return render(request, 'lecturers/timetables.html', {'lecturer': lecturer, 'timetables': timetables})
@login_required
def lecturer_assignments(request):
    lecturer = request.user.lecturerprofile
    units = Unit.objects.filter(lecturer=request.user)
    assignments = Assignment.objects.filter(unit__in=units).order_by('-created_at')

    return render(request, 'lecturers/assignments.html', {
        'assignments': assignments
    })
@login_required
def assignment_submissions(request, assignment_id):
    lecturer = request.user.lecturerprofile
    assignment = get_object_or_404(Assignment, id=assignment_id, unit__lecturer=request.user)
    submissions = Submission.objects.filter(assignment=assignment)

    return render(request, 'lecturers/submissions.html', {
        'assignment': assignment,
        'submissions': submissions,
    })

@login_required
def create_assignment(request):
    lecturer = request.user.lecturerprofile
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            if assignment.unit.lecturer != request.user:
                messages.error(request, "You can only create assignments for your units.")
                return redirect('lecturers:lecturer_assignments')
            assignment.save()
            messages.success(request, "Assignment created successfully.")
            return redirect('lecturers:lecturer_assignments')
    else:
        form = AssignmentForm()

    form.fields['unit'].queryset = Unit.objects.filter(lecturer=request.user)
    return render(request, 'lecturers/create_assignment.html', {'form': form})
from django import forms

class GradeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade', 'feedback']

@login_required
def grade_submission(request, submission_id):
    lecturer = request.user.lecturerprofile
    submission = get_object_or_404(Submission, id=submission_id, assignment__unit__lecturer=request.user)
    
    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, "Grade and feedback saved.")
            return redirect('lecturers:assignment_submissions', assignment_id=submission.assignment.id)
    else:
        form = GradeSubmissionForm(instance=submission)

    return render(request, 'lecturers/grade_submission.html', {
        'form': form,
        'submission': submission
    })
