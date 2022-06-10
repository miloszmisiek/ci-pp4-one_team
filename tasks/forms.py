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
            'end_date'
        ]
        widgets = {
            'end_date': forms.DateTimeInput(),
        }
