from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .models import Mandato, Residente


class MandatoForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Mandato
        fields = ['numero_tarjeta', 'casa_comercial', 'monto', 'start_date']
        labels = {
            'numero_tarjeta': _('Número de tarjeta'),
            'casa_comercial': _('Nombre Casa Comercial'),
            'monto': _('Monto'),
            'start_date': _('Fecha de inicio del mandato'),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date and start_date < timezone.now().date():
            raise forms.ValidationError("La fecha de inicio debe ser hoy o una fecha futura.")
        return start_date


class ResidenteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Residente
        fields = ['nombre_apellido', 'rut', 'nacionalidad', 'fecha_nacimiento', 'estado_civil', 'genero',
                  'direccion', 'comuna', 'celular', 'en_hogar']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'rut': 'RUT',
            'nacionalidad': 'Nacionalidad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'estado_civil': 'Estado Civil',
            'genero': 'Género',
            'direccion': 'Dirección',
            'comuna': 'Comuna',
            'celular': 'Celular',
            'en_hogar': 'En Hogar',
        }

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > timezone.now().date():
            raise forms.ValidationError("La fecha de nacimiento debe ser anterior o igual a la fecha actual.")
        return fecha_nacimiento


class ResidenteDetailForm(forms.ModelForm):
    age = forms.IntegerField(label='Edad')

    class Meta:
        model = Residente
        fields = ['nombre_apellido', 'rut', 'age', 'nacionalidad', 'estado_civil', 'genero',
                  'direccion', 'comuna', 'celular', 'en_hogar']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'rut': 'RUT',
            'age': 'Edad',
            'nacionalidad': 'Nacionalidad',
            'estado_civil': 'Estado Civil',
            'genero': 'Género',
            'direccion': 'Dirección',
            'comuna': 'Comuna',
            'celular': 'Celular',
            'en_hogar': 'En Hogar',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.fecha_nacimiento:
            self.initial['age'] = instance.get_age()

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        if age is None or age <= 0:
            self.add_error('age', 'La edad debe ser un número válido.')
        return cleaned_data