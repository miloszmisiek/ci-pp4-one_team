from django import forms
from .models import Task
from datetime import date


class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'assigned_to',
            'priority',
            'start_date',
            'end_date'
        ]
        widgets = {
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
         self.assigned_to = kwargs.pop('assigned_to', None)
         super(AddTask, self).__init__(*args, **kwargs)
         self.fields['assigned_to'].queryset = self.assigned_to

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater or equal than start date.")
        # if end_date < date.today():
        #     raise forms.ValidationError("End Date should be greater or equal than today's date.")
