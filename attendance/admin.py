from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'employee',
        'date',
        'status',
        'check_in',
        'check_out',
    )

    list_filter = (
        'date',
        'status',
    )

    search_fields = (
        'employee__full_name',
        'employee__email',
    )

    ordering = ('-date',)




