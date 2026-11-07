from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):

    # Fetch all employees
    employees = Employee.objects.all().order_by('-created_at')

    # Count total employees
    total_employees = employees.count()

    context = {
        'employees': employees,
        'total_employees': total_employees,
    }

    return render(request, 'employees.html', context)


def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('employee_list')

    else:

        form = EmployeeForm()

    context = {
        'form': form,
    }

    return render(request, 'add_employee.html', context)
