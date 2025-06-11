from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  
    path('aviso-legal/', views.aviso_legal, name='aviso_legal'), 
    path('politica-de-privaciad/', views.politica_de_privacidad, name='politica_de_privacidad'),  
    path('politica-de-cookies/', views.politica_de_cookies, name='politica_de_cookies'),   
]
