
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from AppRACForms.views import views
from AppRACForms.views  import show_html
from AppRACForms.views import rentacarformulariochofer
from AppRACForms.views import rentacarformulariopasajero

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
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

path('app/',include("AppRACForms.urls")),
path('app/',include("AppRentACar.urls")),
path('show/',show_html),
path('rentacarformulariopasajero', views.rentacarformulariopasajero, name="RentACarFormularioPasajero"),
path('rentacarformulariochofer', views.rentacarformulariochofer, name="RentACarFormulariochofer"),
path('busquedaApellido', views.busquedaApellido, name="BusquedaApellido"),
path('buscar/', views.buscar),
path('login', views.login_request, name= 'Login'),
path('register', views.register, name = 'register'),
path('logout', LogoutView.as_view(template_name= 'AppRACForm/logout.html'), name= 'Logout'),




