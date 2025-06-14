from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Productos  # Usas Productos como lo pediste
from .forms import ProductForm



# Vistas para el CRUD de productos

def index(request):
    """Vista principal (landing page o menú de navegación)."""
    return render(request, 'index.html')


def listar_productos(request):
    """Muestra la lista de productos disponibles y eliminados."""
    productos_disponibles = Productos.objects.all()
    productos_eliminados = Productos.deleted_objects.all()

    context = {
        'listado_disponibles': productos_disponibles,
        'listado_eliminados': productos_eliminados,
    }
    return render(request, 'productos/listar_productos.html', context)


def registrar_producto(request):
    """Registra un nuevo producto."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Producto registrado correctamente.')
            return redirect('listar_prod')
    else:
        form = ProductForm()

    return render(request, 'productos/registrar_producto.html', {'form': form})


def modificar_producto(request, pk):
    """Modifica un producto existente, incluyendo eliminados."""
    producto = get_object_or_404(Productos.all_objects, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Producto modificado correctamente.')
            return redirect('listar_prod')
    else:
        form = ProductForm(instance=producto)

    return render(request, 'productos/modificar_producto.html', {'form': form})


def eliminar_producto(request, pk):
    """Elimina lógicamente un producto."""
    producto = get_object_or_404(Productos.all_objects, pk=pk)
    if request.method == 'POST':
        producto.soft_delete()
        # messages.success(request, f'Producto {producto.codigo} eliminado.')
        return redirect('listar_prod')
    return redirect('listar_prod')  # Podrías también mostrar una página de confirmación aquí


def restaurar_producto(request, pk):
    """Restaura un producto eliminado lógicamente."""
    producto = get_object_or_404(Productos.all_objects, pk=pk)
    if request.method == 'POST':
        producto.restore()
        # messages.success(request, f'Producto {producto.codigo} restaurado.')
        return redirect('listar_prod')
    return redirect('listar_prod')



# def listar_productos(request): # request quiere decir solicitado
#     producto = Productos.objects.all() # la variable (objeto, en este casp) producto recibe todos los atributos que tiene la clase Productos del models.py de la app porductos
#     return render(request, "listar-productos.html", {"listado": producto}) # listar-productos.html es el template. "listado" es la variable que contendrá los datos a mostrar (debe coincidir con la variable utilizada en el html).

# def registrar_producto(request):
#     if (request.method == "POST"): # se verifica la utilización del método POST para los datos enviados.
#         form = ProductForm(request.POST) # se guardan los datos enviados con el método POST en el objeto form
#         if (form.is_valid()): # si los datos recibidos son válidos...
#             form.save() # se guardan los datos
#             return redirect('listar_prod') # se redirecciona a listar_prod (name de la urls)
#     else: # no se utilizó el método POST (sino GET)
#         form = ProductForm() # el objeto form recibe el formulario ProductForm vacío
#     return render(request, 'registrar-productos.html', {"registrar": form}) # registrar es la variable donde se cargarán los datos del formulario (debe coincidir en el html).
   
# def modificar_producto(request, pk): # pk será el valor a buscar para la modificación del registro
#     producto = get_object_or_404(Productos, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
#     if (request.method == 'POST'): # se verifica la utilización del método POST para los datos enviados
#         form = ProductForm(request.POST, instance=producto) # si se usa POST, se guarda en la variable instance lo que contenga producto
#         if (form.is_valid()):
#             form.save() # se guardan los datos
#             return redirect('listar_prod') # se redirecciona a listar_prod (name de la urls)
#     else: # no se utilizó el método POST (sino GET)
#         form = ProductForm(instance=producto) # se carga el formulario con los datos encontrados
#     return render(request, 'modificar-productos.html', {'modificar': form}) # modificar es la variable donde se cargarán los datos del formulario (debe coincidir en el html).

# def eliminar_producto(request, pk): # pk será el valor a buscar para la eliminación del registro
#     producto = get_object_or_404(Productos, pk=pk) # si no se encuentra el producto, se lanza una página con el error 404
#     producto.delete() # borra el registro encontrado
#     return redirect('listar_prod') # redirecciona al listar_productos.html