
from django.shortcuts import render, redirect, get_object_or_404

from employees.models import Employee
from .models import Department
from .forms import DepartmentForm


# ==========================================
# VIEW ALL DEPARTMENTS + SEARCH
# ==========================================

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
            department=department.name
        ).count()

    context = {
        'departments': departments,
        'total_departments': Department.objects.count(),
        'search_query': search_query,
    }

    return render(
        request,
        'department_list.html',
        context
    )


# ==========================================
# ADD DEPARTMENT
# ==========================================

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


# ==========================================
# EDIT DEPARTMENT
# ==========================================

def edit_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    old_name = department.name

    if request.method == 'POST':

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():

            updated_department = form.save()

            # Update existing employees if department name changes
            if old_name != updated_department.name:

                Employee.objects.filter(
                    department=old_name
                ).update(
                    department=updated_department.name
                )

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


# ==========================================
# DELETE DEPARTMENT
# ==========================================

def delete_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    employee_count = Employee.objects.filter(
        department=department.name
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
