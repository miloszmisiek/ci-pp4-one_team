from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """Custom Admin Panel Users Model"""
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User rank',
            {
                'fields': (
                    'rank',
                )
            }
        )
    )

    list_display = ('first_name', 'last_name', 'rank', 'is_active')
    actions = ['activate_user_account']

    def activate_user_account(self, request, queryset):
        """Method to activate users with inactive accounts"""
        queryset.update(is_active=True)

admin.site.register(CustomUser, CustomUserAdmin)
