from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    """Custom user model."""
    # Roles to assign to users
    ROLES = [
        (0, 'Master'),
        (1, 'Senior Officer'),
        (2, 'Junior Officer'),
        (3, 'Bosun'),
    ]
    RANK_STATUS = (
        (0, 'Approved'),
        (1, 'Denied'),
        )

    username = models.CharField(
        max_length=50, blank=False,
        null=True,
        unique=True
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    rank = models.IntegerField(choices=ROLES, blank=False, null=False, default=None)

    def get_rank_choices(self):
        """Return rank choices."""
        return dict(self.ROLES)[self.rank]

    def __str__(self):
        """Return string representation of user."""
        return str(self.username)

    class Meta:
        """Meta class"""
        ordering = ['email']
