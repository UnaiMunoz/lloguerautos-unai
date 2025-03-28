import os
import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from faker import Faker
import random
from datetime import timedelta

class Command(BaseCommand):
    help = "Seeds the database with sample data without deleting existing records"

    def handle(self, *args, **kwargs):
        # Inicializar Faker
        fake = Faker("es_ES")

        # Crear Automóviles
        self.stdout.write(self.style.WARNING("Creating Automobiles..."))
        automobils = list(Automobil.objects.all())  # Mantener coches existentes
        car_models = [
            ("Seat", "León"),
            ("Volkswagen", "Golf"),
            ("BMW", "3 Series"),
            ("Mercedes-Benz", "Clase A"),
        ]

        matriculas_existentes = set(Automobil.objects.values_list("matricula", flat=True))

        for _ in range(4):  # Agregar 4 coches más en cada ejecución
            marca, model = random.choice(car_models)

            # Asegurar matrículas únicas
            matricula = fake.license_plate()
            while matricula in matriculas_existentes:
                matricula = fake.license_plate()
            matriculas_existentes.add(matricula)

            automobil = Automobil.objects.create(
                marca=marca, model=model, matricula=matricula
            )
            automobils.append(automobil)

        self.stdout.write(self.style.SUCCESS(f"✅ Now there are {len(automobils)} automobiles"))

        # Crear Usuarios
        self.stdout.write(self.style.WARNING("Creating Users..."))
        users = list(User.objects.filter(is_superuser=False))  # Mantener usuarios existentes

        for _ in range(8):  # Agregar 8 usuarios más en cada ejecución
            username = fake.user_name()
            while User.objects.filter(username=username).exists():
                username = fake.user_name()

            user = User.objects.create_user(
                username=username, email=fake.email(), password="testpass123"
            )
            users.append(user)

        self.stdout.write(self.style.SUCCESS(f"✅ Now there are {len(users)} users"))

        # Crear Reservas
        self.stdout.write(self.style.WARNING("Creating Reservations..."))

        existing_reservations = set(
            Reserva.objects.values_list("automobil_id", "data_inici")
        )

        for user in users:
            num_reservas = random.randint(1, 2)

            for _ in range(num_reservas):
                for _ in range(10):  # Intentar hasta 10 veces encontrar una fecha libre
                    automobil = random.choice(automobils)
                    data_inici = fake.date_between(start_date="-2m", end_date="+2m")
                    data_fi = data_inici + timedelta(days=random.randint(1, 7))

                    # Verificar que la reserva no existe ya
                    if (automobil.id, data_inici) not in existing_reservations:
                        Reserva.objects.create(
                            automobil=automobil,
                            usuari=user,
                            data_inici=data_inici,
                            data_fi=data_fi,
                        )
                        existing_reservations.add((automobil.id, data_inici))
                        break

        self.stdout.write(self.style.SUCCESS(f"✅ Now there are {Reserva.objects.count()} reservations"))

        # Mostrar estadísticas finales
        self.stdout.write(f"📊 Total Automobiles: {Automobil.objects.count()}")
        self.stdout.write(f"👤 Total Users: {User.objects.filter(is_superuser=False).count()}")
        self.stdout.write(f"📅 Total Reservations: {Reserva.objects.count()}")
