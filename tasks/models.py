from django.db import models
from users.models import CustomUser
import datetime

DEFAULT_TASK_ID = 1
TASK_STATUS = (
    (0, "Scheduled"),
    (1, "Completed"),
    (2, "Overdue"),
)

TASK_PRIORITY = (
    (0, "High"),
    (1, "Medium"),
    (2, "Low"),
)

TASK_APPROVAL = (
    (0, "Approved"),
    (1, "Waiting For Approval"),
    (2, "N/R"),
)


class Task(models.Model):
    """Custom Task Model"""

    title = models.CharField(max_length=35, blank=False, default="Untitled Task")
    description = models.TextField(max_length=300, blank=True)
    status = models.IntegerField(choices=TASK_STATUS, default=0)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="task_creator", null=True
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="task_owner",
    )
    priority = models.IntegerField(choices=TASK_PRIORITY, default=2)
    approval_status = models.IntegerField(choices=TASK_APPROVAL, default=1)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)

    class Meta:
        """Subclass for Metadata"""

        ordering = ["end_date"]

    def __str__(self):
        """String representation of Task instances"""
        return self.title

    def duration(self):
        """Returns time delta between End Date and Start Date in days"""
        return (self.end_date - self.start_date).days

    def is_past_due(self):
        """Returns tuple with boolean value of End Date lesser than current date and time delta of End Date and today's date"""
        return (
            datetime.date.today() > self.end_date,
            (self.end_date - datetime.date.today()).days,
        )

    def updated_on_time(self):
        """Returns time delta of today's date and Updated On date in days"""
        return (datetime.date.today() - self.updated_on).days
