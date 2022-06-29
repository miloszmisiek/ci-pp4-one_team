from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
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
        queryset.update(is_active=True)

admin.site.register(CustomUser, CustomUserAdmin)
