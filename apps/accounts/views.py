from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to view the dashboard.")
        return redirect('user_login')
    return render(request, 'dashboard.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User.objects.create_user(username=username, password=password)
        return redirect('user_login')
    
    return render(request, 'auth/register.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid credentials!')
    
    return render(request, 'auth/login.html')


def user_logout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to logout.")
        return redirect('user_login')
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('user_login')