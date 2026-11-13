from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from employees.models import Employee
from .models import Department
from .forms import DepartmentForm


# VIEW ALL DEPARTMENTS + SEARCH

@login_required
def department_list(request):

    departments = Department.objects.all().order_by('name')

    search_query = request.GET.get('q', '').strip()

    if search_query:
        departments = departments.filter(
            name__icontains=search_query
        )

    # Count employees in every department
    for department in departments:
        department.employee_count = Employee.objects.filter(
            department=department
        ).count()

    context = {
        'departments': departments,
        'total_departments': Department.objects.count(),
        'search_query': search_query,
    }

    return render(request, 'department_list.html', context)


# ADD DEPARTMENT

@login_required
def add_department(request):

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('department_list')

    else:
        form = DepartmentForm()

    return render(
        request,
        'department_form.html',
        {
            'form': form,
            'title': 'Add Department'
        }
    )


# EDIT DEPARTMENT

@login_required
def edit_department(request, pk):

    department = get_object_or_404(Department, pk=pk)

    if request.method == 'POST':
        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():
            form.save()
            return redirect('department_list')

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        'department_form.html',
        {
            'form': form,
            'title': 'Edit Department',
            'department': department
        }
    )


# DELETE DEPARTMENT

@login_required
def delete_department(request, pk):

    department = get_object_or_404(Department, pk=pk)

    employee_count = Employee.objects.filter(
        department=department
    ).count()

    error = None

    if request.method == 'POST':

        if employee_count > 0:
            error = (
                'This department has employees assigned to it. '
                'Reassign those employees before deleting it.'
            )

        else:
            department.delete()
            return redirect('department_list')

    context = {
        'department': department,
        'employee_count': employee_count,
        'error': error,
    }

    return render(
        request,
        'department_confirm_delete.html',
        context
    )
