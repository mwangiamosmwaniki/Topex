from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ResultForm
from .models import Result
from admissions.models import Applicant

# Restrict to staff users
@user_passes_test(lambda u: u.is_staff)
def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results:view_results')
    else:
        form = ResultForm()
    return render(request, 'results/add_result.html', {'form': form})

# Require login
@login_required
def view_results(request):
    results = Result.objects.select_related('applicant', 'course').order_by('-date_recorded')
    return render(request, 'results/view_results.html', {'results': results})

# Require login
@login_required
def student_results(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    results = Result.objects.filter(applicant=applicant).order_by('academic_year', 'semester')
    return render(request, 'results/student_results.html', {'applicant': applicant, 'results': results})
