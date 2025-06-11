from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario
from resident.models import Resident
from tecnico.models import Tecnico
from django.views.decorators.cache import never_cache


def redirect_by_role(usuario, request):
    rol = usuario.rol.nombre.lower()

    if rol == 'residente':
        try:
            residente = Resident.objects.get(user=usuario)
            request.session['user_name'] = f"{residente.first_name} {residente.last_name1}"
        except Resident.DoesNotExist:
            request.session['user_name'] = usuario.email  # fallback
        return redirect('resident_dashboard')

    elif rol == 'técnico':
        try:
            tecnico = Tecnico.objects.get(user=usuario)
            request.session['user_name'] = f"{tecnico.first_name} {tecnico.last_name1}"
        except Tecnico.DoesNotExist:
            request.session['user_name'] = usuario.email
        return redirect('tecno_dashboard')

    else:
        return redirect('home')




@never_cache
def login_view(request):
    error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                usuario = Usuario.objects.get(email=email)
                if usuario.check_password(password):
                    request.session['usuario_email'] = usuario.email
                    request.session['usuario_rol'] = usuario.rol.nombre

                    return redirect_by_role(usuario, request)

                else:
                    error = "Lo sentimos, la contraseña no coincide."
            except Usuario.DoesNotExist:
                error = "Lo sentimos, el correo no está registrado."
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form, 'error': error})

def logout_view(request):
    request.session.flush()
    return redirect('login')
