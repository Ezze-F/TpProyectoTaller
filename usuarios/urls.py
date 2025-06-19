from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('', inicio_sesion, name='sesion'),
]