from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student-registration/', views.student_registration, name='student_registration'),
    path('student-login/', views.student_login, name='student_login'),
    path('staff-registration/', views.staff_registration, name='staff_registration'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('admin-registration/', views.admin_registration, name='admin_registration'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
]
