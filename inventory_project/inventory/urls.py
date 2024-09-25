# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   path('', views.assignment_list, name='assignment_list'),
   path('admin/assignments/', views.admin_assignment_list, name='admin_assignment_list'),
   path('admin/assign-equipment/', views.assign_equipment, name='assign_equipment'),
]