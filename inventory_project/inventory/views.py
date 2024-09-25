from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Assignment, EmployeeProfile, Equipment  # Ensure these are correctly imported

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('assignment_list')  # Redirect to the assignment list after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'inventory/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'inventory/home.html')

@login_required
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'inventory/equipment_list.html', {'equipment': equipment})

@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(employee__user=request.user)
    return render(request, 'inventory/assignment_list.html', {'assignments': assignments})

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'inventory/admin_assignment_list.html', {'assignments': assignments})

@user_passes_test(is_admin)
def assign_equipment(request):
    if request.method == 'POST':
        employee_id = request.POST['employee']
        equipment_id = request.POST['equipment']
        employee = EmployeeProfile.objects.get(id=employee_id)
        equipment = Equipment.objects.get(id=equipment_id)
        Assignment.objects.create(employee=employee, equipment=equipment)
        messages.success(request, f"{equipment.name} assigned to {employee.user.username}.")
        return redirect('admin_assignment_list')
    else:
        employees = EmployeeProfile.objects.all()
        equipment = Equipment.objects.all()
        return render(request, 'inventory/assign_equipment.html', {'employees': employees, 'equipment': equipment})