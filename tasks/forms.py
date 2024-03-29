from django import forms
from .models import Task


class AddTask(forms.ModelForm):
    """Add Task form build on Task model"""

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "assigned_to",
            "priority",
            "start_date",
            "end_date",
        ]
        widgets = {
            "end_date": forms.widgets.DateInput(attrs={"type": "date"}),
            "start_date": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        self.assigned_to = kwargs.pop("assigned_to", None)
        super(AddTask, self).__init__(*args, **kwargs)
        self.fields["assigned_to"].empty_label = None
        self.fields["assigned_to"].required = True
        self.fields["assigned_to"].queryset = self.assigned_to

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError(
                "End date should be greater or equal than start date."
            )
