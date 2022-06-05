from django.db import models

# Create your models here.
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
    # slug = models.SlugField(max_length=100, blank=False)
    description = models.TextField(max_length=300, blank=True)
    status = models.IntegerField(choices=TASK_STATUS, default=0)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name='users',
        null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


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
