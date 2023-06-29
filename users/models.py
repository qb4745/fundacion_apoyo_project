from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MinLengthValidator

import datetime


User = get_user_model()

class Mandato(models.Model):
    MODALIDAD_CHOICES = [
        ('AbcVisa', 'AbcVisa'),
        ('Falabella', 'Falabella'),
        ('Hites', 'Hites'),
        ('La Polar', 'La Polar'),
        ('Paris', 'Paris'),
        ('Ripley', 'Ripley'),
    ]

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16, unique=True, validators=[MinLengthValidator(16)])
    casa_comercial = models.CharField(max_length=50, choices=MODALIDAD_CHOICES)
    monto = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # must be positive
    modalidad = models.CharField(max_length=50, default='Mensual')
    start_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.numero_tarjeta} - {self.casa_comercial} - {self.monto} - {self.modalidad}")

    def get_absolute_url(self):
        return reverse("users:users-mandato", kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse("users:users-mandato-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("users:users-mandato-delete", kwargs={'pk': self.pk})

    def get_last_digits(self):
        last_four_digits = self.numero_tarjeta[-4:]
        return "**** **** **** " + last_four_digits

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Retrieve the request object from kwargs
        if not self.pk:  # Check if the instance is being created
            if request and request.user.is_authenticated:
                # Set the user field as the logged-in user
                self.user = request.user
        super().save(*args, **kwargs)


GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

ESTADO_CIVIL_CHOICES = (
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('V', 'Viudo/a'),
    )

class Residente(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50, default='Chileno/a')
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    en_hogar = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_apellido

    def get_absolute_url(self):
        return reverse("users:users-residente-list")

    def get_update_url(self):
        return reverse("users:users-residente-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("users:users-residente-delete", kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse("users:users-residente-detail", kwargs={'pk': self.pk})

    def get_age(self):
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)


class Fichamedica(models.Model):
    residente = models.OneToOneField(Residente, on_delete=models.CASCADE)
    presion_arterial = models.CharField(max_length=20)
    alergias = models.TextField()
    condiciones_medicas = models.TextField()
    medicamentos = models.TextField()

    def __str__(self):
        return self.residente.nombre_apellido
