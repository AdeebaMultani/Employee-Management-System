from django.db import models
from django.utils import timezone
from employees.models import Employee


class Attendance(models.Model):

    # Attendance status choices
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    # Employee relationship
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    # Attendance date
    date = models.DateField(default=timezone.localdate)

    # Attendance status
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Present'
    )

    # Check-in and check-out timings
    check_in = models.TimeField(
        null=True,
        blank=True
    )

    check_out = models.TimeField(
        null=True,
        blank=True
    )

    # Additional remarks
    remarks = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'date'],
                name='unique_employee_attendance_per_day'
            )
        ]

    def __str__(self):
        return f"{self.employee.full_name} - {self.date} - {self.status}"
