from django.contrib import admin
from .models import Rol, Usuario

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Para mostrar el nombre en la lista

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'rol')
    search_fields = ('email',)
    list_filter = ('rol',)
