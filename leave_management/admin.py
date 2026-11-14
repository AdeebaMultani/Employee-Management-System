from django.contrib import admin
from .models import LeaveRequest


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'employee',
        'leave_type',
        'start_date',
        'end_date',
        'status',
        'applied_at',
    )

    list_filter = (
        'leave_type',
        'status',
        'start_date',
    )

    search_fields = (
        'employee__full_name',
        'leave_type',
        'reason',
    )

    ordering = ('-applied_at',)
