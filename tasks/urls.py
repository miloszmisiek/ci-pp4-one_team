from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_home, name='tasks'),
    path('my_tasks/', views.my_tasks, name='my_tasks'),
    path('create/', views.add_task, name='add_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('approve/<task_id>', views.approve_task, name='approve'),
    path('complete/<task_id>', views.complete_task, name='complete'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
]
