from django.shortcuts import render, redirect, get_object_or_404 # render es para renderizar (mostrar una pantalla html). redirect para redireccionar a otra vista. get_object_or_404 para mostrar el mensaje de error 404
from productos.models import * # Se importan todas las clases (entidades) que contiene el models.py de la app productos
from .forms import ProductForm # se importa el formulario ProductForm para generar la vista
# el . antes de forms indica que forms.py se encuentra al mismo nivel (misma carpeta) que el views.py de la app

# Create your views here.

# Este CRUD utiliza el models.py de esta app (productos)

def listar_productos(request): # request quiere decir solicitado
    producto = Productos.objects.all() # la variable (objeto, en este casp) producto recibe todos los atributos que tiene la clase Productos del models.py de la app porductos
    return render(request, "listar-productos.html", {"listado": producto}) # listar-productos.html es el template. "listado" es la variable que contendrá los datos a mostrar (debe coincidir con la variable utilizada en el html).

def registrar_producto(request):
    if (request.method == "POST"): # se verifica la utilización del método POST para los datos enviados.
        form = ProductForm(request.POST) # se guardan los datos enviados con el método POST en el objeto form
        if (form.is_valid()): # si los datos recibidos son válidos...
            form.save() # se guardan los datos
            return redirect('listar_prod') # se redirecciona a listar_prod (name de la urls)
    else: # no se utilizó el método POST (sino GET)
        form = ProductForm() # el objeto form recibe el formulario ProductForm vacío
    return render(request, 'registrar-productos.html', {"registrar": form}) # registrar es la variable donde se cargarán los datos del formulario (debe coincidir en el html).
   
def modificar_producto(request, pk): # pk será el valor a buscar para la modificación del registro
    producto = get_object_or_404(Productos, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
    if (request.method == 'POST'): # se verifica la utilización del método POST para los datos enviados
        form = ProductForm(request.POST, instance=producto) # si se usa POST, se guarda en la variable instance lo que contenga producto
        if (form.is_valid()):
            form.save() # se guardan los datos
            return redirect('listar_prod') # se redirecciona a listar_prod (name de la urls)
    else: # no se utilizó el método POST (sino GET)
        form = ProductForm(instance=producto) # se carga el formulario con los datos encontrados
    return render(request, 'modificar-productos.html', {'modificar': form}) # modificar es la variable donde se cargarán los datos del formulario (debe coincidir en el html).

def eliminar_producto(request, pk): # pk será el valor a buscar para la eliminación del registro
    producto = get_object_or_404(Productos, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
    producto.delete() # borra el registro encontrado
    return redirect('listar_prod') # redirecciona al listar_productos.html