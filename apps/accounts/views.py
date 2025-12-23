from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User.objects.create_user(username, password)
        return redirect('home')
    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Succesfully loged in!')
        else:
            return HttpResponse('Invalid credentials!')
    
    return render(request, 'auth/login.html')