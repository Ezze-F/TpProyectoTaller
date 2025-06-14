from django.urls import path
from productos.views import (
    index,
    listar_productos,
    registrar_producto,
    modificar_producto,
    eliminar_producto,
    restaurar_producto,
)

urlpatterns = [
    path("", index, name='inicio'),

    path('listar/', listar_productos, name='listar_prod'),
    path('registrar/', registrar_producto, name='registrar_prod'),
    path('<int:pk>/modificar/', modificar_producto, name='modificar_prod'),
    path('<int:pk>/eliminar/', eliminar_producto, name='eliminar_prod'),
    path('<int:pk>/restaurar/', restaurar_producto, name='restaurar_prod'),  # ✅ Ruta añadida
]