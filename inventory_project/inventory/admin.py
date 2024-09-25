# inventory/admin.py
from django.contrib import admin
from .models import EmployeeProfile, Equipment, Assignment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Unregister the default User admin
admin.site.unregister(User)

# Register User without any inlines (since we're not using EmployeeProfile inline)
admin.site.register(User, BaseUserAdmin)

# Register your models
admin.site.register(EmployeeProfile)
admin.site.register(Equipment)
admin.site.register(Assignment)