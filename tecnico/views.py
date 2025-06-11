from django.shortcuts import render, redirect
from .models import Tecnico 
from authentication.models import Usuario 
# Create your views here.

def dashboard(request):
    if 'usuario_email' not in request.session:
        return redirect('login')

    user_name = request.session.get('user_name', 'Tecnico')  # obtienes el nombre guardado en sesión o un fallback

    return render(request, 'tecnico/dashboard.html', {'user_name': user_name})



def profile_view(request):
    if 'usuario_email' not in request.session:
        return redirect('login')

    try:
        usuario_email = request.session['usuario_email']
        usuario = Usuario.objects.get(email=usuario_email)
        tecnico = Tecnico.objects.get(user=usuario)
    except (Usuario.DoesNotExist, Tecnico.DoesNotExist):
        tecnico = None

    return render(request, 'tecnico/profile.html', {
        'tecnico': tecnico
    })