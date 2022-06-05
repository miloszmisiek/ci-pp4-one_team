from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """Custom user model."""
    # Roles to assign to users
    ROLES = (
        (0, 'master'),
        (1, 'senior officer'),
        (2, 'junior officer'),
        (3, 'bosun'),
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
    phone = models.CharField(max_length=30, blank=False, null=False)
    role = models.IntegerField(choices=ROLES, default=5)

    def get_role_choices(self):
        """Return role choices."""
        return dict(self.ROLES)[self.role]

    def __str__(self):
        """Return string representation of user."""
        return str(self.username)

    class Meta:
        """Meta class"""
        ordering = ['email']