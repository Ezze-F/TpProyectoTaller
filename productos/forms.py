from django import forms # importamos la librería forms para poder utilizarla
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos # el objeto model va a ser del tipo Productos (entidad que pertenece a models.py)
        fields = "__all__" # se van a utilizar todos los campos
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