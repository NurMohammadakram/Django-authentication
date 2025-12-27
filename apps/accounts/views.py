from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User.objects.create_user(username=username, password=password)
        return redirect('user_login')
    
    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('Succesfully loged in!')
        else:
            return HttpResponse('Invalid credentials!')
    
    return render(request, 'auth/login.html')