from django.urls import path
from productos.views import *
# from productos.views import (index, listar_productos,
#     registrar_producto,
#     modificar_producto,
#     eliminar_producto,
#     restaurar_producto,
# )

urlpatterns = [
    path("", index, name='inicio'), # "" es la ruta donde se carga la funcionalidad "index" del views.py con el nombre "inicio"
    path('listar/', listar_productos, name='listar_prod'), # "listar/" es la ruta donde se carga la funcionalidad "listrar_productos" del views.py con el nombre "listar_prod"
    path('registrar/', registrar_producto, name='registrar_prod'), # "registrar/" es la ruta donde se carga la funcionalidad "registrar_producto" del views.py con el nombre "registrar_prod"
    path('<int:pk>/modificar/', modificar_producto, name='modificar_prod'), # "modificar/" es la ruta donde se carga la funcionalidad "modificar_producto" del views.py con el nombre "modificar_prod". Se le pasa pk para que la funcionalidad trabaje con ella.
    path('<int:pk>/eliminar/', eliminar_producto, name='eliminar_prod'), # "eliminar/" es la ruta donde se carga la funcionalidad "eliminar_producto" del views.py con el nombre "eliminar_prod". Se le pasa pk para que la funcionalidad trabaje con ella.
    path('<int:pk>/restaurar/', restaurar_producto, name='restaurar_prod'), # "restaurar/" es la ruta donde se carga la funcionalidad "restaurar_producto" del views.py con el nombre "restaurar_prod"
]