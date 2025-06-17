from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Productos
from .forms import ProductForm


def index(request):
    # Vista principal
    return render(request, 'index.html')

def listar_productos(request): # request quiere decir solicitado
    # Muestra la lista de productos disponibles y eliminados.
    productos_disponibles = Productos.objects.all() # el objeto productos_disponibles recibe todos los atributos que tiene la clase Productos del models.py de la app productos excluyendo los eliminados lógicamente.
    productos_eliminados = Productos.deleted_objects.all() # el objeto productos_eliminados recibe todos los atributos que tiene la clase Productos del models.py de la app productos que fueron eliminados lógicamente.
    context = {
        'listado_disponibles': productos_disponibles,
        'listado_eliminados': productos_eliminados,
    }
    return render(request, 'productos/listar_productos.html', context) # renderiza en la ruta 'productos/listar_productos.html' las dos pestañas que contiene context.

def registrar_producto(request):
    # Registra un nuevo producto.
    if (request.method == 'POST'): # se verifica la utilización del método POST para los datos enviados.
        form = ProductForm(request.POST) # se guardan los datos enviados con el método POST en el objeto form
        if form.is_valid(): # si los datos recibidos son válidos...
            form.save() # se guardan los datos
            # Se podría agregar el mensaje: messages.success(request, 'Producto registrado correctamente.')
            return redirect('listar_prod') # se redirecciona a listar_prod (nombre de la urls)
    else: # no se utilizó el método POST (sino GET)
        form = ProductForm() # el objeto form recibe el formulario ProductForm vacío
    return render(request, 'productos/registrar_producto.html', {'form': form}) # 'form' es la variable donde se cargarán los datos del formulario (debe coincidir en el html).

def modificar_producto(request, pk): # pk será el valor a buscar para la modificación del registro
    # Modifica un producto existente, incluyendo eliminados.
    producto = get_object_or_404(Productos.all_objects, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
    if (request.method == 'POST'): # se verifica la utilización del método POST para los datos enviados
        form = ProductForm(request.POST, instance=producto) # si se usa POST, se guarda en la variable instance lo que contenga producto
        if form.is_valid(): # si los datos recibidos son válidos...
            form.save() # se guardan los datos
            # Se podría agregar el mensaje: messages.success(request, 'Producto modificado correctamente.')
            return redirect('listar_prod') # se redirecciona a listar_prod (nombre de la urls)
    else: # no se utilizó el método POST (sino GET)
        form = ProductForm(instance=producto) # se carga el formulario con los datos encontrados
    return render(request, 'productos/modificar_producto.html', {'form': form}) # 'form'' es la variable donde se cargarán los datos del formulario (debe coincidir en el html).

def eliminar_producto(request, pk): # pk será el valor a buscar para la eliminación del registro
    # Elimina lógicamente un producto.
    producto = get_object_or_404(Productos.all_objects, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
    if (request.method == 'POST'): # se verifica la utilización del método POST para los datos enviados
        producto.soft_delete() # se utiliza el método sof_delete() para borrar lógicamente el registro
        # Se podría agregar el mensaje: messages.success(request, f'Producto {producto.codigo} eliminado.')
        return redirect('listar_prod') # redirecciona al listar_productos.html (Aquí se podría mostrar un mensaje de eliminación correcta)
    return redirect('listar_prod') # redirecciona al listar_productos.html 

def restaurar_producto(request, pk): # pk será el valor a buscar para la eliminación del registro
    # Restaura un producto eliminado lógicamente.
    producto = get_object_or_404(Productos.all_objects, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
    if request.method == 'POST': # se verifica la utilización del método POST para los datos enviados
        producto.restore() # se utiliza el método restore() para restaurar el registro borrado lógicamente-
        # Se podría agregar el mensaje: messages.success(request, f'Producto {producto.codigo} restaurado.')
        return redirect('listar_prod') # redirecciona al listar_productos.html (Aquí se podría mostrar un mensaje de restauración correcta)
    return redirect('listar_prod') # redirecciona al listar_productos.html 


