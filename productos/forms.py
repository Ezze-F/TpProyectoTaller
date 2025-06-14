from django import forms
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        # Incluye todos los campos excepto los que no deberían ser editables manualmente
        exclude = ['codigo', 'is_deleted', 'deleted_at']  # ← añadimos los campos internos

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
