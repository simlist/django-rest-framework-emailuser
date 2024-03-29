from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmailUserCreationForm, EmailUserChangeForm


class EmailUserAdmin(UserAdmin):
    add_form = EmailUserCreationForm
    form = EmailUserChangeForm
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('email', 'name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'name',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            )
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('name',)


admin.site.register(get_user_model(), EmailUserAdmin)
