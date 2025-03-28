from django.contrib import admin
from .models import Automobil

@admin.register(Automobil)
class AutomobilAdmin(admin.ModelAdmin):
    # Especificar qué campos se mostrarán en el listado de objetos
    list_display = ('matricula', 'marca', 'model')
    
    # Opcional: añadir campos de búsqueda
    search_fields = ('matricula', 'marca', 'model')