from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def student_login(request):
    if request.user.is_authenticated:
        return redirect('student_portal:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and hasattr(user, 'studentprofile'):
            login(request, user)
            return redirect('student_portal:dashboard')
        else:
            messages.error(request, 'Invalid credentials or not a student account.')

    return render(request, 'student_portal/login.html')


def student_logout(request):
    logout(request)
    return redirect('student_portal:login')

@login_required
def dashboard(request):
    profile = StudentProfile.objects.get(user=request.user)
    payments = Payment.objects.filter(student=request.user)
    billing = BillingStatement.objects.filter(student=request.user)
    transcript = Transcript.objects.filter(student=request.user)
    return render(request, 'student_portal/dashboard.html', {
        'profile': profile,
        'payments': payments[:5],
        'billing': billing[:5],
        'transcript': transcript[:5],
    })

@login_required
def payment_history(request):
    payments = Payment.objects.filter(student=request.user).order_by('-payment_date')
    return render(request, 'student_portal/payment_history.html', {'payments': payments})

@login_required
def fee_structure(request):
    structures = FeeStructure.objects.all()
    return render(request, 'student_portal/fee_structure.html', {'structures': structures})

@login_required
def semester_registration(request):
    if request.method == 'POST':
        semester = request.POST.get('semester')  # safer access
        if not semester:
            messages.error(request, "Please select a semester.")
            return redirect('student_portal:semester_registration')

        SemesterRegistration.objects.create(student=request.user, semester=semester)
        messages.success(request, "Semester registered successfully.")
        return redirect('student_portal:dashboard')

    return render(request, 'student_portal/semester_registration.html')


@login_required
def transcript(request):
    transcript = Transcript.objects.filter(student=request.user)
    return render(request, 'student_portal/transcript.html', {'transcript': transcript})

@login_required
def profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'student_portal/profile.html', {'profile': profile})
from .forms import StudentProfileForm  # Ensure this import is at the top

@login_required
def edit_profile(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('student_portal:dashboard')
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'student_portal/edit_profile.html', {'form': form})
