from django.shortcuts import render
from resident.models import Testimonio

# Create your views here.
def home(request):
    
    testimonios = Testimonio.objects.filter(aprobado=True).select_related('residente')[:3]
    return render(request, 'core/home.html', {'testimonios': testimonios})


def about(request):
    return render(request, 'core/about.html')

def aviso_legal(request):
    return render(request, 'core/aviso_legal.html')


def politica_de_privacidad(request):
    return render(request, 'core/politica_privacidad.html')


def politica_de_cookies(request):
    return render(request, 'core/politica_cookies.html')

