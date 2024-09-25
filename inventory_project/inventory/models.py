# inventory/models.py
from django.contrib.auth.models import User
from django.db import models

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

class Assignment(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment} assigned to {self.employee}"