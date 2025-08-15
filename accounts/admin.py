from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

# Register your models here.
class UserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('id',)

admin.site.register(User, UserAdmin)