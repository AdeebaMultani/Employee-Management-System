from django import forms
from .models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):

    class Meta:
        model = LeaveRequest

        fields = [
            'employee',
            'leave_type',
            'start_date',
            'end_date',
            'reason',
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'end_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'reason': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter reason for leave'
                }
            ),
        }
        
        def clean(self):
            cleaned_data = super().clean()

            employee = cleaned_data.get('employee')
            start_date = cleaned_data.get('start_date')
            end_date = cleaned_data.get('end_date')

            # Check date order
            if start_date and end_date and end_date < start_date:
                raise forms.ValidationError("End date cannot be before start date.")

            # Check overlapping leave requests
            if employee and start_date and end_date:
                overlapping_leaves = LeaveRequest.objects.filter(
                employee=employee,
                start_date__lte=end_date,
                end_date__gte=start_date).exclude(status='Rejected')

            # Exclude the current request when editing
            if self.instance.pk:
                overlapping_leaves = overlapping_leaves.exclude(pk=self.instance.pk)

            if overlapping_leaves.exists():
                raise forms.ValidationError("This employee already has a pending or approved "
                                            "leave request during these dates."
            )
            
            return cleaned_data

