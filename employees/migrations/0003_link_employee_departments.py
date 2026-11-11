from django.db import migrations


def link_departments(apps, schema_editor):
    Employee = apps.get_model('employees', 'Employee')
    Department = apps.get_model('departments', 'Department')

    for employee in Employee.objects.all():
        department = Department.objects.filter(
            name__iexact=employee.department.strip()
        ).first()

        if department:
            employee.department_ref = department
            employee.save(update_fields=['department_ref'])
        else:
            raise ValueError(
                f"No matching Department found for employee: {employee.full_name}"
            )


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_department_ref'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            link_departments,
            migrations.RunPython.noop
        ),
    ]
