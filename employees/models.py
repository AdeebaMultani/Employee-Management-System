from django.db import models


class Employee(models.Model):

    # Basic employee information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    # Job information
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    # Joining information
    joining_date = models.DateField()

    # Salary
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    # Employee photo
    photo = models.ImageField(
        upload_to='employees/',
        blank=True,
        null=True
    )

    # Automatically store when employee was added
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name