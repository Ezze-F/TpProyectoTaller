from django import forms # importamos la librería forms para poder utilizarla
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos # el objeto model va a ser del tipo Productos (entidad que pertenece a models.py)
        fields = "__all__" # se van a utilizar todos los campos
        labels = { # etiquetas para que se muestren en los modals
            'preciounitario': 'Precio unitario',
            'marca': 'Marca del producto',
            'cantidad': 'Cantidad disponible',
            'fechaelaboracion': 'Fecha de elaboración',
            'fechavencimiento': 'Fecha de vencimiento',
            'descripcion': 'Descripción del producto',
        }
        exclude = ['codigo', 'is_deleted', 'deleted_at']  # campos excluidos
        widgets = {
            'fechaelaboracion': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'fechavencimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'preciounitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
