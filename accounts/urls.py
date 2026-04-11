"""
URL configuration for Resell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('admin_home/', views.admin_home, name='admin_home'),
    path('login/',views.Login, name='login'),  # login page
    path('register/',views.Register, name='register'),
    path('logout/',views.Logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('restricted/',views.admin_restricted, name='admin_restricted'),
    path('captcha/refresh/', views.refresh_captcha, name='captcha-refresh'),
    path('captcha/', include('captcha.urls')),
]

     

