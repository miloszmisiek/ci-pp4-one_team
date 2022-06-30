from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Custom Admin Panel Model for Task"""
    list_display = (
        "title",
        "status",
        "approval_status",
        "created_by",
        "priority",
        "assigned_to",
        "created_on",
        "updated_on",
        "start_date",
        "end_date",
    )
    list_filter = ("status", "end_date")
    actions = ["approve_tasks"]

    def approve_tasks(self, request, queryset):
        """Approving task method used in the Actions bar"""
        queryset.update(approval_status=0)
