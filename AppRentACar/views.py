import contextlib
from operator import index
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return HttpResponse("vista inicio")

def pasajero(request):
    return HttpResponse("vista pasajero")

def chofer(request):
    return HttpResponse("vista chofer")

def viaje(request):
    return HttpResponse("vista viaje")

def show_html(request):
    return render (request, "index.html", contextlib) 
