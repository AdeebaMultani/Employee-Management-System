import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('employees', '0003_link_employee_departments'),
    ]

    operations = [
        # Remove the old text-based department field.
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),

        # Rename the existing ForeignKey without losing its data.
        migrations.RenameField(
            model_name='employee',
            old_name='department_ref',
            new_name='department',
        ),

        # Keep the relationship nullable for now.
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='employees',
                to='departments.department',
            ),
        ),
    ]
