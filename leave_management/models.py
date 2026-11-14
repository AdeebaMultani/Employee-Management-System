from django.db import models
from employees.models import Employee


class LeaveRequest(models.Model):

    LEAVE_TYPES = [
        ('Casual', 'Casual Leave'),
        ('Sick', 'Sick Leave'),
        ('Earned', 'Earned Leave'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='leave_requests'
    )

    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES
    )

    start_date = models.DateField()
    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type}"

    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1
    
