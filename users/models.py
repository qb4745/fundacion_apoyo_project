from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

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
    numero_tarjeta = models.CharField(max_length=16)
    casa_comercial = models.CharField(max_length=50, choices=MODALIDAD_CHOICES)
    monto = models.IntegerField(default=0)
    modalidad = models.CharField(max_length=50, default='Mensual')
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
