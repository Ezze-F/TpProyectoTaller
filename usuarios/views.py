from django.shortcuts import render, redirect
from usuarios.models import Usuarios
from .forms import UserForm

def login_view(request):
    return render(request, 'usuarios/login.html')

# Create your views here.
def inicio_sesion(request):
    error = None
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave']
            try:
                usuario = Usuarios.objects.get(nombre=nombre, clave=clave)
                # Guardar en la sesión
                request.session['usuario_id'] = usuario.codigo
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('inicio')  # o a la página que quieras
            except Usuarios.DoesNotExist:
                error = "Usuario o clave incorrectos."
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form, 'error': error})