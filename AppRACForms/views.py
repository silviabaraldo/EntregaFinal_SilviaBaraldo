import contextlib
from operator import index
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def rentacarformulariopasajero(request):
    if request.method == 'POST':
       miformulario = rentacarformulariopasajero(request.POST)
       print(miformulario)
       if miformulario.is_valid: 
          informacion = miformulario.cleaned_data 
          pasajero = rentacarformulariopasajero(nombre=informacion['pasajero'], email=informacion ['email'])
          pasajero.save() 
          
          return render(request,"AppRACform/rentacarformulariopasajero.html")
    
    else: 
        miformulario = rentacarformulariopasajero()
    
        return render(request, "AppRACform/rentacarformulariopasajero.html"),({"miformulario": miformulario})

def rentacarformulariochofer(request):
    if request.method == 'POST':
       miformulario = rentacarformulariochofer(request.POST)
       print(miformulario)
       if miformulario.is_valid: 
          informacion = miformulario.cleaned_data 
          chofer = rentacarformulariochofer(nombre=informacion['chofer'], apellido=informacion ['apellido'])
          chofer.save() 
          
          return render(request,"AppRACform/rentacarformulariochofer.html")
    
    else: 
        miformulario = rentacarformulariochofer()
    
        return render(request, "AppRACform/rentacarformulariochofer.html"),({"miformulario": miformulario})


def busquedaApellido (request):
    return render(request, "AppRACform/busquedaapellido.html")

def buscar(request):
    respuesta = f"Buscar apellido: {request.GET['apellido']}"
    return HttpResponse(respuesta)
    
    if request.GET["apellido"]:
       apellido = request.GET['apellido']
       chofer = chofer.objetcs.filter(apellido)(_icontains=apellido) 
       return render(request,"AppRACform/busquedaapellido.html", {"chofer":chofer, "apellido": busquedaApellido})
    
def login_request(request):
    
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contra)
                
                if user is not None: 
                    login(request, user)
                    return render(request, "AppRentACar/index.html", {"mensaje": f"Bienvenido {usuario}"})
                
                else:
                    return render(request, "AppRentACar/inicio.html", {"mensaje":"datos erróneos"}) 
            
      else:
                    return render(request,"AppRentACar/inicio.html", {"mensaje":"datos erróneos"})
      
      form = AuthenticationForm()
      return render(request,"AppRentACar/inicio.html", {'form': form})


def register(request):
      if request.method == "POST":     
           form = UserCreationForm(request.POST)
           if form.is_valid():
                username= form.cleaned_data['username']
                form.save()
                return render(request, "AppRentACar/inicio.html", {"mensaje":"Usuario creado"})
      else:
                form = UserCreationForm()

      return render (request, "AppRentACar/registro.html",  {"form":form})