import contextlib
from operator import index
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from AppRentACar.models import Viaje

def inicio(request):
    return HttpResponse("vista inicio")

def pasajero(request):
    return HttpResponse("vista pasajero")

def chofer(request):
    return HttpResponse("vista chofer")

def viaje(request):
    return HttpResponse("vista viaje")

def show_html(request):
    contexto= {"nombre": "Silvia"}
    return render (request, "index.html", contexto) 

def crear_pasajero_form(request):
    return render

def crear_viaje(request):
    viaje = Viaje (destino="Capital", barrio="La Boca")
    viaje.save()
    contexto ={"viaje": viaje}

def mostrar_viajes(request):
   viajes= viaje.objects.all()
   contexto = {
        "viajes": viajes
    }
   return render(request, template_name= "AppRentACar/viajes.html"- contexto)