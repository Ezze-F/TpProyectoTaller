from django.shortcuts import render, redirect # render es para renderizar. redirect
from productos.models import * # Se importan todas las clases (entidades) que contiene el models.py de la app productos
from .forms import ProductForm # se importa el formulario ProductForm para generar la vista
# el . antes de forms indica que forms.py se encuentra al mismo nivel (misma carpeta) que el views.py

# Create your views here.

# Este CRUD utiliza el models.py de esta app (productos)

def listar_productos(request): # request quiere decir solicitado
    producto = Productos.objects.all() # la variable (objeto, en este casp) producto recibe todos los atributos que tiene la clase Productos del models.py de la app porductos
    return render(request, "listar-productos.html", {"listado": producto}) # listar-productos.html es el template. "listado" es la variable que contendrá los datos a mostrar (debe coincidir con la variable utilizada en el html).

def registrar_productos(request):
    if (request.method == "POST"): # se verifica la utilización del método POST para los datos enviados.
        form = ProductForm(request.POST) # se guardan los datos enviados con el método POST en el objeto form
        if (form.is_valid()): # si los datos recibidos son válidos...
            form.save() # se guardan los datos
            return redirect('listar_prod') # se redirecciona a listar_prod (name de la urls)
    else: # no se utilizó el método POST (sino GET)
        form = ProductForm() # el objeto form recibe el formulario ProductForm vacío
    return render(request, 'registrar-productos.html', {"registrar": form}) # registrar es la variable donde se cargarán los datos del formulario (debe coincidir en el html).
   
def modificar_productos(request):
    
    return render()