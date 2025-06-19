from django import forms # importamos la librería forms para poder utilizarla
from .models import Usuarios

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios # el objeto model va a ser del tipo Productos (entidad que pertenece a models.py)
        fields = "__all__" # se van a utilizar todos los campos
        exclude = ['codigo']  # campos excluidos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control'}),
        }