
from django.urls import include, path
from AppRentACar import views
from AppRACForms import views
from AppRentACar.views import show_html
from AppRentACar.views import mostrar_viajes

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

path('app/',include("AppRentACar.urls")),
path('app/',include("AppRACForms.urls")),
path("",views.inicio), 
path('pasajero',views.pasajero,name="Pasajero"),
path('chofer', views.chofer),
path('viaje', views.viaje),
path('show/', show_html),
path ('viajes', mostrar_viajes)
