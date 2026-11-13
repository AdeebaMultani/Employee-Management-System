from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from django.utils.dateparse import parse_date
from employees.models import Employee
from .models import Attendance
from .forms import AttendanceForm


@login_required
def attendance_list(request):

    today = timezone.localdate()

    # All attendance records
    attendances = Attendance.objects.select_related(
        'employee',
        'employee__department'
    ).all()

    # Search by employee name
    search_query = request.GET.get('q', '').strip()

    if search_query:
        attendances = attendances.filter(
            Q(employee__full_name__icontains=search_query) |
            Q(employee__email__icontains=search_query)
        )

    # Filter by date
    selected_date = request.GET.get('date', '').strip()
    parsed_date = parse_date(selected_date)

    if parsed_date:
        attendances = attendances.filter(date=parsed_date)

    # Filter by status
    selected_status = request.GET.get('status', '').strip()

    if selected_status in ['Present', 'Absent', 'Late']:
        attendances = attendances.filter(
            status=selected_status
        )

    # Dashboard statistics - always for today
    today_attendances = Attendance.objects.filter(date=today)

    context = {
        'attendances': attendances.order_by('-date', 'employee__full_name'),
        'total_records': attendances.count(),

        'total_employees': Employee.objects.count(),

        'present_count': today_attendances.filter(
            status='Present'
        ).count(),

        'absent_count': today_attendances.filter(
            status='Absent'
        ).count(),

        'late_count': today_attendances.filter(
            status='Late'
        ).count(),

        'today': today,

        # Filter values
        'search_query': search_query,
        'selected_date': selected_date,
        'selected_status': selected_status,
    }

    return render(
        request,
        'attendance/attendance_list.html',
        context
    )



@login_required
def mark_attendance(request):

    if request.method == 'POST':
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'attendance/mark_attendance.html',
        {'form': form}
    )


@login_required
def edit_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm(instance=attendance)

    context = {
        'form': form,
        'attendance': attendance,
        'title': 'Edit Attendance',
    }

    return render(
        request,
        'attendance/mark_attendance.html',
        context
    )


@login_required
def delete_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')

    return render(
        request,
        'attendance/delete_attendance.html',
        {'attendance': attendance}
    )
