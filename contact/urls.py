# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),  # La vista del formulario de contacto
    
]
