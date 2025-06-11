from django.contrib import admin
from .models import Tecnico

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name1', 'oficio', 'gender', 'phone')
    list_filter = ('oficio', 'gender')
    search_fields = ('first_name', 'last_name1', 'last_name2', 'identity_document', 'phone')
