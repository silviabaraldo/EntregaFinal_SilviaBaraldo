"""
URL configuration for TerceraEntrega_SilviaBaraldo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')path
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django import views
from django.urls import path, include
from TerceraEntrega_SilviaBaraldo.views import saludo, saludo_template1, saludo_template2

urlpatterns = [
    path('bienvenida', saludo_template2),           
    path('templaterentcar/', saludo_template1),      
    path('saludo/',saludo),          
    path('admin/',admin.site.urls) ,
    path('app/',include('AppRentACar.urls')),
    path('app/',include('AppRACForms.urls'))
     
                         
















]
