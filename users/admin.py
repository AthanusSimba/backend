from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {  # all fields
            'fields': ('email', 'username', 'is_farmer', 'is_general', 'is_scientist',
                       'is_government', 'is_admin', 'is_supplier', 'password1', 'password2')
        }),
        ('Permissions', {  # permissions fields
            'fields': ('is_superuser', 'is_staff')
        }),
    )
    fieldsets = (
        ('None', {  # user display once created
            'fields': ('email', 'username', 'is_farmer', 'is_general', 'is_scientist',
                       'is_government', 'is_admin', 'is_supplier', 'password')
        }),
        ('Permissions', {  # permissions fields
            'fields': ('is_superuser', 'is_staff')
        }),
    )
    list_display = ['email', 'username', 'is_farmer', 'is_general', 'is_scientist',
                    'is_government', 'is_admin', 'is_supplier', 'is_superuser']
    search_fields = ['email', 'username']
    ordering = ['email']
    list_editable = ['is_farmer', 'is_general', 'is_scientist', 'is_government', 'is_admin', 'is_supplier']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
