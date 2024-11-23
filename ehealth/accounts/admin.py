# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'phone_number', 'user_type', 'is_active', 'is_staff')
#     list_filter = ('is_active', 'user_type', 'is_staff', 'is_superuser', 'date_joined')
#     search_fields = ('email', 'first_name', 'last_name', 'username', 'phone_number')
#     ordering = ('date_joined',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_photo')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Roles', {'fields': ('user_type',)}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2'),
#         }),
#     )

#     def user_type_display(self, obj):
#         return obj.get_user_type_display()
#     user_type_display.short_description = "User Type"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'user_type', 'is_active', 'is_staff')
    list_filter = ('is_active', 'user_type', 'is_staff', 'is_superuser', 'date_joined','is_admin','is_hospital')
    search_fields = ('email', 'first_name', 'last_name', 'username', 'phone_number')
    ordering = ('date_joined',)

    readonly_fields = ('date_joined', 'last_login',)  # Mark non-editable fields as readonly

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin','is_hospital','groups', 'user_permissions',)}),
        ('Roles', {'fields': ('user_type',)}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),  # Keep here but as readonly
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2'),
        }),
    )



from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage

class MyAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': [staticfiles_storage.url('accounts/admin.css')],
        }
