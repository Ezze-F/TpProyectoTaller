from django import forms # importamos la librería forms para poder utilizarla
from productos.models import *


class ProductForm(forms.ModelForm): # se crea la clase ProductForm utilizando ModelForm de la librería forms
    class Meta:
        model = Productos # el objeto model va a ser del tipo Productos (entidad que pertenece a models.py)
        fields = "__all__" # se van a utilizar todos los campos
        exclude = ['codigo'] # excluye al campo codigo al momento de registrar un nuevo producto ya que será autoincremental (configuración realizada en Workbench)
        widgets = {
            'fechaelaboracion': forms.DateInput(attrs={'type': 'date'}), # genera un input date (calendario) para el registro de un nuevo producto
            'fechavencimiento': forms.DateInput(attrs={'type': 'date'}), # genera un input date (calendario) para el registro de un nuevo producto
        }
