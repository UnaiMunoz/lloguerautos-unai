from django.shortcuts import render
from .models import Automobil, Reserva

def view_automobils(request):
    # Obtener todos los automóviles
    automobils = Automobil.objects.all()

    # Pasar los automóviles al contexto de la plantilla
    return render(request, 'lloguer/automobils_list.html', {'automobils': automobils})

def view_reservas(request):
    # Obtener todas las reservas
    reservas = Reserva.objects.all()

    # Pasar las reservas al contexto de la plantilla
    return render(request, 'lloguer/reservas_list.html', {'reservas': reservas})