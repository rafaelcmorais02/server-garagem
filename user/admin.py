from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    ordering = ('-created_at',)
    list_display = ('user_name', 'first_name', 'is_active',
                    'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
