from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from academics.models import Assignment, Submission
from django.utils import timezone
from .forms import ContactForm
from lecturers.models import LecturerProfile  # Make sure this import is correct
from django.shortcuts import get_object_or_404
from .models import ContactInfo

def home(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'core/home.html', {'contact_info': contact_info})


def about(request):
    return render(request, 'core/about.html')

@login_required
def dashboard(request):
    role = request.user.profile.role
    if role == 'student':
        return redirect('student_dashboard')
    elif role == 'lecturer':
        return redirect('lecturer_dashboard')
    elif role == 'admin':
        return redirect('/admin/')
    return HttpResponseForbidden("Unrecognized role.")

@login_required(login_url='/users/login/')
def student_dashboard(request):
    if request.user.profile.role != 'student':
        return HttpResponseForbidden("Access denied.")
    return render(request, 'core/student_dashboard.html', {'student': request.user})

@login_required
def lecturer_dashboard(request):
    try:
        lecturer_profile = LecturerProfile.objects.get(user=request.user)
    except LecturerProfile.DoesNotExist:
        return HttpResponseForbidden("Access denied.")

    return render(request, 'lecturers/dashboard.html', {'lecturer': lecturer_profile})

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = ContactForm(data)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

                send_mail(
                    subject=f"Contact Form Message from {name}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['mwangiamos703@gmail.com'],
                    fail_silently=False,
                )

                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid input. Please fill all fields correctly.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def available_assignments(request):
    units = request.user.enrolled_units.all()
    assignments = Assignment.objects.filter(unit__in=units).order_by('-due_date')

    submissions = Submission.objects.filter(student=request.user, assignment__in=assignments)
    submissions_dict = {sub.assignment_id: sub for sub in submissions}

    return render(request, 'core/available_assignments.html', {
        'assignments': assignments,
        'submissions_dict': submissions_dict,
    })


@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        submission, created = Submission.objects.update_or_create(
            assignment=assignment,
            student=request.user,
            defaults={'file': file, 'submitted_at': timezone.now()}
        )
        messages.success(request, 'Assignment submitted successfully.')
        return redirect('core:available_assignments')

    return render(request, 'core/submit_assignment.html', {'assignment': assignment})
