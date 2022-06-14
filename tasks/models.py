from django.db import models
from users.models import CustomUser

DEFAULT_TASK_ID = 1

# task model variables

TASK_STATUS = (
    (0, 'In Progress'),
    (1, 'Completed'),
)

TASK_PRIORITY = (
    (0, 'High'),
    (1, 'Medium'),
    (2, 'Low'),
)

TASK_APPROVAL = (
    (0, 'Approved'),
    (1, 'Waiting For Approval'),
    (2, 'Approval Not Required')
)


class Task(models.Model):
    title = models.CharField(
        max_length=35,
        blank=False,
        default='Untitled Task'
        )
    description = models.TextField(max_length=300, blank=True)
    status = models.IntegerField(choices=TASK_STATUS, default=0)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name='task_creator',
        null=True
        )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='task_owner'
    )
    priority = models.IntegerField(choices=TASK_PRIORITY, default=2)
    approval_status = models.IntegerField(choices=TASK_APPROVAL, default=1)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def duration(self):
        return (self.end_date - self.created_on).days

class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=False,
    )
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='written_comments',
    )
    comment_body = models.TextField(max_length=300, blank=False, default='')
    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        editable=False
        )
    updated_on = models.DateTimeField(
        auto_now=True,
        blank=False,
        editable=False
        )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment_body
