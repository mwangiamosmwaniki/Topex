from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department, Program, Unit
from django.db.models import Q
from django.core.paginator import Paginator


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'academics/departments.html', {'departments': departments})


def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, 'academics/program_detail.html', {'program': program})

@login_required
def unit_detail(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    return render(request, 'academics/unit_detail.html', {'unit': unit})

@login_required
def unit_search(request):
    query = request.GET.get('q', '')
    program_id = request.GET.get('program', '')

    units = Unit.objects.all()
    if query:
        units = units.filter(title__icontains=query)
    if program_id:
        units = units.filter(program__id=program_id)

    paginator = Paginator(units, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    programs = Program.objects.all()

    return render(request, 'academics/unit_search.html', {
        'query': query,
        'programs': programs,
        'page_obj': page_obj,
    })

@login_required
def enroll_in_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    unit.enrolled_users.add(request.user)
    return redirect('academics:unit_search')

@login_required
def enrolled_units(request):
    user = request.user
    units = Unit.objects.filter(enrolled_users=user)

    return render(request, 'academics/enrolled_units.html', {
        'units': units,
    })
@login_required
def unenroll_from_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    if request.user in unit.enrolled_users.all():
        unit.enrolled_users.remove(request.user)
    return redirect('academics:enrolled_units')
