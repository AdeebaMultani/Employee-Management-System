from django.shortcuts import render
from django.db.models import Count
from employees.models import Employee


def dashboard(request):

    # Total employees
    total_employees = Employee.objects.count()

    # Total unique departments
    total_departments = Employee.objects.values(
        'department'
    ).distinct().count()

    # Latest 5 employees
    recent_employees = Employee.objects.order_by(
        '-created_at'
    )[:5]

    # Department-wise employee count
    departments = Employee.objects.values(
        'department'
    ).annotate(
        total=Count('id')
    ).order_by('-total')

    # Calculate department percentages
    department_data = []

    for dept in departments:

        percentage = (
            round((dept['total'] / total_employees) * 100)
            if total_employees > 0 else 0
        )

        department_data.append({
            'name': dept['department'] or 'Not specified',
            'total': dept['total'],
            'percentage': percentage,
        })

    # Send data to dashboard.html
    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'recent_employees': recent_employees,
        'department_data': department_data,
    }

    return render(request, 'dashboard.html', context)
