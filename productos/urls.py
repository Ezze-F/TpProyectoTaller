from django.urls import path
#from productos.views import *
from . import views

urlpatterns = [
    path('listar/', views.listar_productos, name='listar_prod'), # "listar/" es la ruta donde se carga la funcionalidad "listrar_productos" del views.py con el nombre "listar_prod"
    path('registrar/', views.registrar_producto, name='registrar_prod'), # "registrar/" es la ruta donde se carga la funcionalidad "registrar_producto" del views.py con el nombre "registrar_prod"
    path('<int:pk>/modificar/', views.modificar_producto, name='modificar_prod'), # "modificar/" es la ruta donde se carga la funcionalidad "modificar_producto" del views.py con el nombre "modificar_prod". Se le pasa pk para que la funcionalidad trabaje con ella.
    path('<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_prod'), # "eliminar/" es la ruta donde se carga la funcionalidad "eliminar_producto" del views.py con el nombre "eliminar_prod". Se le pasa pk para que la funcionalidad trabaje con ella.
    path('<int:pk>/restaurar/', views.restaurar_producto, name='restaurar_prod'), # "restaurar/" es la ruta donde se carga la funcionalidad "restaurar_producto" del views.py con el nombre "restaurar_prod"

    path("reporte/", views.reporte_producto_pdf, name="reporteProducto"),

]