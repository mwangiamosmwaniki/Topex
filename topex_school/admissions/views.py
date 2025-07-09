from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Applicant, Application
from django.urls import reverse

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            applicant = Applicant.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )
            Application.objects.create(
                applicant=applicant,
                course=form.cleaned_data['course']
            )
            # Redirect to dashboard for that applicant
            return redirect(reverse('admissions:dashboard', args=[applicant.id]))
    else:
        form = ApplicationForm()
    return render(request, 'admissions/apply.html', {'form': form})


def success(request):
    return render(request, 'admissions/success.html')


def dashboard(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    applications = Application.objects.filter(applicant=applicant).order_by('-date_applied')
    return render(request, 'admissions/dashboard.html', {
        'applicant': applicant,
        'applications': applications
    })
