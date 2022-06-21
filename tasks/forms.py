from django import forms
from .models import Task


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
