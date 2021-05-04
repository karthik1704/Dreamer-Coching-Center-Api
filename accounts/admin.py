from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('username', 'email', 'pk', 'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_student')
    search_fields = ('username',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('pk',)
    filter_horizontal = ()
    list_filter = ('is_student',)
    fieldsets = (
        ('Account Information', {
            'fields': ('username', 'email', 'password'),
        }),
        ('Personal Information', {
            'fields': ('first_name','last_name'),
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_active','is_staff', 'is_student'),
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ( 'username', 'email', 'password1', 'password2'),
        }),
        ('Personal Information', {
            'fields': ('first_name','last_name'),
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_active','is_staff', 'is_student'),
        }),
    )


admin.site.register(User, CustomUserAdmin)