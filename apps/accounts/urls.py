from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login')
]