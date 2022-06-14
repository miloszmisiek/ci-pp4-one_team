from django import forms
from django.contrib.admin import widgets
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
    # def __init__(self, *args, **kwargs):
    #      self.assigned_to = kwargs.pop('assigned_to',None)
    #      super(AddTask, self).__init__(*args, **kwargs)
