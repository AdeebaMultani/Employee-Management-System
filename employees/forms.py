from django import forms
from .models import Employee
from departments.models import Department


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
            'department': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'salary': forms.NumberInput(
                attrs={'step': '0.01'}
            ),

            'photo': forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['department'].queryset = Department.objects.order_by('name')
        self.fields['department'].empty_label = 'Select Department'
