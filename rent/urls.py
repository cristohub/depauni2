from django.urls import path
from . import views

urlpatterns = [
     path('departamentos/', views.departamentos_disponibles, name='departamentos'),
     path('departamento/<int:id>/', views.detalle_departamento, name='detalle_departamento'),
   
]