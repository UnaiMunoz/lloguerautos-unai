from django.urls import path
from . import views

urlpatterns = [
    path('autos/', views.view_automobils, name='automobils_list'),
    path('reservas/', views.view_reservas, name='reservas_list'),
]
