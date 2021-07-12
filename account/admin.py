from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'password',
    ]
    list_display = ('username', 'first_name', 'email', 'is_active')
    list_filter = ('is_active',)
    ordering = ['first_name']
