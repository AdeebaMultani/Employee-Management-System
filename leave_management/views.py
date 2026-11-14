from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from employees.models import Employee
from .forms import LeaveRequestForm
from django.db.models import OuterRef, Subquery
from .models import LeaveRequest


def apply_leave(request):

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Leave application submitted successfully!'
            )
            return redirect('leave_list')

    else:
        form = LeaveRequestForm()

    return render(
        request,
        'leave_management/apply_leave.html',
        {'form': form}
    )

def leave_list(request):

    # Get all leave requests
    leaves = LeaveRequest.objects.select_related(
        'employee'
    ).order_by('-applied_at')

    # SEARCH
    search_query = request.GET.get('q', '')

    if search_query:
        leaves = leaves.filter(
            employee__full_name__icontains=search_query
        )

    # STATUS FILTER
    selected_status = request.GET.get('status', '')

    if selected_status:
        leaves = leaves.filter(status=selected_status)

    # LEAVE TYPE FILTER
    selected_type = request.GET.get('leave_type', '')

    if selected_type:
        leaves = leaves.filter(leave_type=selected_type)

    # GET ONLY THE LATEST LEAVE REQUEST FOR EACH EMPLOYEE
    latest_leave = leaves.filter(
        employee=OuterRef('employee')
    ).order_by('-applied_at').values('id')[:1]

    leaves = leaves.filter(
        id=Subquery(latest_leave)
    ).order_by('-applied_at')

    # DASHBOARD STATISTICS
    total_requests = LeaveRequest.objects.count()

    pending_count = LeaveRequest.objects.filter(
        status='Pending'
    ).count()

    approved_count = LeaveRequest.objects.filter(
        status='Approved'
    ).count()

    rejected_count = LeaveRequest.objects.filter(
        status='Rejected'
    ).count()

    context = {
        'leaves': leaves,
        'total_requests': total_requests,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'search_query': search_query,
        'selected_status': selected_status,
        'selected_type': selected_type,
    }

    return render(
        request,
        'leave_management/leave_list.html',
        context
    )


@staff_member_required
@require_POST
def approve_leave(request, leave_id):

    leave = get_object_or_404(LeaveRequest, id=leave_id)

    if leave.status == 'Pending':
        leave.status = 'Approved'
        leave.save(update_fields=['status'])

        messages.success(
            request,
            'Leave request approved successfully!'
        )
    else:
        messages.warning(
            request,
            'This leave request has already been processed.'
        )

    return redirect('leave_list')


@staff_member_required
@require_POST
def reject_leave(request, leave_id):

    leave = get_object_or_404(LeaveRequest, id=leave_id)

    if leave.status == 'Pending':
        leave.status = 'Rejected'
        leave.save(update_fields=['status'])

        messages.success(
            request,
            'Leave request rejected successfully!'
        )
    else:
        messages.warning(
            request,
            'This leave request has already been processed.'
        )

    return redirect('leave_list')

@staff_member_required
def employee_leave_history(request, employee_id):

    employee = get_object_or_404(Employee, id=employee_id)

    leaves = LeaveRequest.objects.filter(
        employee=employee
    ).order_by('-applied_at')

    total_requests = leaves.count()

    pending_count = leaves.filter(
        status='Pending'
    ).count()

    approved_count = leaves.filter(
        status='Approved'
    ).count()

    rejected_count = leaves.filter(
        status='Rejected'
    ).count()

    context = {
        'employee': employee,
        'leaves': leaves,
        'total_requests': total_requests,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
    }

    return render(
        request,
        'leave_management/employee_leave_history.html',
        context
    )

@staff_member_required
def edit_leave(request, leave_id):

    leave = get_object_or_404(LeaveRequest, id=leave_id)

    if leave.status != 'Pending':
        messages.warning(
            request,
            'Only pending leave requests can be edited.'
        )
        return redirect('leave_list')

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Leave request updated successfully!'
            )

            return redirect('leave_list')

    else:
        form = LeaveRequestForm(instance=leave)

    return render(
        request,
        'leave_management/edit_leave.html',
        {
            'form': form,
            'leave': leave
        }
    )


@staff_member_required
@require_POST
def delete_leave(request, leave_id):

    leave = get_object_or_404(LeaveRequest, id=leave_id)

    if leave.status != 'Pending':
        messages.warning(
            request,
            'Only pending leave requests can be deleted.'
        )
    else:
        leave.delete()

        messages.success(
            request,
            'Leave request deleted successfully!'
        )

    return redirect('leave_list')