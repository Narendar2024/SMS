from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def student_registration(request):
    return render(request, 'student_registration.html')

def student_login(request):
    return render(request, 'student_login.html')

def staff_registration(request):
    return render(request, 'staff_registration.html')

def staff_login(request):
    return render(request, 'staff_login.html')

def admin_registration(request):
    return render(request, 'admin_registration.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
