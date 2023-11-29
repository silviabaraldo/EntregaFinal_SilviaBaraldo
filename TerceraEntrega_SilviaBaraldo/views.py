from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("<b>Bienvenido cliente</b>") 

def saludo_template1(request):
    contexto = {
        "nombre":"Silvia",
        "cliente":"corporativo",
        "Edad": 50
        }
{  "nombre": "Ernesto",
                  "cliente": "particular",
                    "edad":"16",
         
         } 

def saludo_template2(request):
    contexto = {
        "nombre" : "Silvia"
    }
    return render(request, "index.html",contexto)
     