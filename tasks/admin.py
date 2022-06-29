from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'approval_status', 'created_by', 'priority', 'assigned_to', 'created_on', 'end_date' )
    list_filter = ('status', 'end_date')
    actions = ['approve_tasks']

    def approve_tasks(self, request, queryset):
        queryset.update(approval_status=0)