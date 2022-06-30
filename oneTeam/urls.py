from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/password/change/",
        users_views.CustomPasswordChangeView.as_view(),
        name="account_change_password",
    ),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
    path("session_security/", include("session_security.urls")),
]
