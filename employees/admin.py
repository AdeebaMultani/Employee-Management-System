from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'department',
        'designation',
        'joining_date',
        'salary',
    )

    search_fields = (
        'full_name',
        'email',
        'department',
        'designation',
    )