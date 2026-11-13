
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Employee
from .forms import EmployeeForm
from departments.models import Department


@login_required
def employee_list(request):

    employees = Employee.objects.select_related('department').all()

    # Search functionality
    search_query = request.GET.get('q', '').strip()

    if search_query:
        employees = employees.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(department__name__icontains=search_query) |
            Q(designation__icontains=search_query)
        )

    # Department filter
    selected_department = request.GET.get('department', '').strip()

    if selected_department:
        employees = employees.filter(
            department__name=selected_department
        )

    # Alphabetical ordering
    employees = employees.order_by('full_name')

    departments = Department.objects.order_by('name')

    context = {
        'employees': employees,
        'total_employees': Employee.objects.count(),
        'departments': departments,
        'search_query': search_query,
        'selected_department': selected_department,
    }

    return render(request, 'employees.html', context)


@login_required
def add_employee(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})


@login_required
def employee_detail(request, pk):

    employee = get_object_or_404(
        Employee.objects.select_related('department'),
        pk=pk
    )

    return render(
        request,
        'employee_detail.html',
        {'employee': employee}
    )


@login_required
def edit_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee,
    }

    return render(request, 'edit_employee.html', context)


@login_required
def delete_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(
        request,
        'delete_employee.html',
        {'employee': employee}
    )
