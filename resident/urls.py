from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='resident_dashboard'),

    path('perfil/', views.profile_view, name='profile'),

    path('payment/', views.payment_view, name='payment'),

    path('lease/', views.lease_view, name='lease'),

]

