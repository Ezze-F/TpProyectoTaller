from django.urls import path
from inicio.views import *

urlpatterns = [
    path("", index, name='inicio'), # "" es la ruta donde se carga la funcionalidad "index" del views.py con el nombre "inicio"
]