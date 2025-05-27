from django.contrib import admin
from django.urls import path
from productos.views import index, listar_productos, registrar_producto, modificar_producto, eliminar_producto

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", index, name='inicio'),
    path('listar/', listar_productos, name='listar_prod'), # 'listar/' ruta en la que se va a mostrar. listar_productos nombre de la vista creada en views. listar_prod nombre asociado a la view.
    path('registrar/', registrar_producto, name='registrar_prod'), # 'registrar/' ruta en la que se va a mostrar. registrar_producto nombre de la vista creada en views. registrar_prod nombre asociado a la view.
    path('<int:pk>/modificar/', modificar_producto, name='modificar_prod'), # 'modificar/' ruta en la que se va a mostrar. modificar_producto nombre de la vista creada en views. modificar_prod nombre asociado a la view.
    path('<int:pk>/eliminar/', eliminar_producto, name='eliminar_prod'), # 'eliminar/' ruta en la que se va a mostrar. eliminar_producto nombre de la vista creada en views. eliminar_prod nombre asociado a la view.
]