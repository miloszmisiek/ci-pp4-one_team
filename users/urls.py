from django.urls import path
from . import views

urlpatterns = [
    path("no_permission/<user_id>", views.edit_profile, name="no_permission"),
    path("edit_profile/<user_id>", views.edit_profile, name="edit_profile"),
    path("delete_profile/<user_id>", views.delete_profile, name="delete_profile"),
]
