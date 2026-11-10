from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter department name'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Enter department description',
                'rows': 4
            }),
        }
