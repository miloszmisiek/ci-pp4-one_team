from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_home, name='tasks'),
    path('create/', views.add_task, name='add_task'),
]
