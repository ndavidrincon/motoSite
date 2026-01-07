from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    def has_delete_permission(self, request, obj=None):
        # Bloquear eliminación del usuario ndavidrincon
        if obj and obj.is_superuser:
            return False

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_superuser:
            return (
                "password",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        return super().get_readonly_fields(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
