from django.contrib import admin
from .models import Automobil, Reserva

@admin.register(Automobil)
class AutomobilAdmin(admin.ModelAdmin):
    # Especificar qué campos se mostrarán en el listado de objetos
    list_display = ('matricula', 'marca', 'model')
    
    # Opcional: añadir campos de búsqueda
    search_fields = ('matricula', 'marca', 'model')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'usuari', 'data_inici', 'data_fi')
    list_filter = ('data_inici', 'data_fi')
    search_fields = ('usuari__username', 'automobil__matricula')