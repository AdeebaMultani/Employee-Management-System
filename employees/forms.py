
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            'full_name',
            'email',
            'phone',
            'department',
            'designation',
            'joining_date',
            'salary',
            'photo',
        ]

        widgets = {
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'salary': forms.NumberInput(
                attrs={'step': '0.01'}
            ),

            'photo': forms.ClearableFileInput(),
        }
