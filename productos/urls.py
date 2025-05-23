from django.contrib import admin
from django.urls import path
from productos.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('listar/', listar_productos, name='listar_prod'), # 'listar/' ruta en la que se va a mostrar. listar_productos nombre de la vista creada en views. listar_prod nombre asociado a la view.
    path('registrar/', registrar_productos, name='registrar_prod')
]