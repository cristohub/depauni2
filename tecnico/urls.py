from django.urls import path
from . import views

urlpatterns = [
    path('dashboard-tec/', views.dashboard, name='tecno_dashboard'),

    path('perfil-tec/', views.profile_view, name='tecno_dashboard'),

]

