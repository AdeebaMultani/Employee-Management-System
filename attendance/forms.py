from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance

        fields = [
            'employee',
            'date',
            'status',
            'check_in',
            'check_out',
            'remarks',
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'check_in': forms.TimeInput(
                attrs={'type': 'time'}
            ),

            'check_out': forms.TimeInput(
                attrs={'type': 'time'}
            ),

            'remarks': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter additional remarks...'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        employee = cleaned_data.get('employee')
        date = cleaned_data.get('date')

        if employee and date:
            existing = Attendance.objects.filter(
                employee=employee,
                date=date
            ).exclude(pk=self.instance.pk)

            if existing.exists():
                raise forms.ValidationError(
                    'Attendance for this employee on this date already exists.'
                )

        return cleaned_data
