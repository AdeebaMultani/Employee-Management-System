from django.shortcuts import render
from .models import Employee


def employee_list(request):

    # Fetch all employees from the database
    employees = Employee.objects.all().order_by('-created_at')

    # Count total employees
    total_employees = employees.count()

    context = {
        'employees': employees,
        'total_employees': total_employees,
    }

    return render(request, 'employees.html', context)