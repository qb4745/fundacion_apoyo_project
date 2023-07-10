from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .models import Mandato, Residente, Medicamento, PlanMedicacion, DosisMedicamento


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
    fecha_admision = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Residente
        fields = ['nombre_apellido', 'rut', 'nacionalidad', 'fecha_nacimiento', 'estado_civil', 'genero',
                  'direccion', 'comuna', 'celular', 'fecha_admision']
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
            'fecha_admision': 'Fecha de Admisión',
        }

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > timezone.now().date():
            raise forms.ValidationError("La fecha de nacimiento debe ser anterior o igual a la fecha actual.")
        return fecha_nacimiento

    def clean_fecha_admision(self):
        fecha_admision = self.cleaned_data.get('fecha_admision')
        if fecha_admision and fecha_admision > timezone.now().date():
            raise forms.ValidationError("La fecha de admisión debe ser anterior o igual a la fecha actual.")
        return fecha_admision


class ResidenteDetailForm(forms.ModelForm):
    age = forms.IntegerField(label='Edad')

    class Meta:
        model = Residente
        fields = ['nombre_apellido', 'rut', 'age', 'nacionalidad', 'estado_civil', 'genero',
                  'direccion', 'comuna', 'celular', 'fecha_admision']
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
            'fecha_admision': 'Fecha de Admisión',
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


class ResidentIngresoEgresoForm(forms.ModelForm):
    fecha_egreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Residente
        fields = ['nombre_apellido', 'rut', 'estado_en_hogar', 'fecha_admision', 'fecha_egreso']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'rut': 'RUT',
            'estado_en_hogar': 'Estado en Hogar',
            'fecha_admision': 'Fecha de Admisión',
            'fecha_egreso': 'Fecha de Egreso',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_egreso'].required = False

    def clean_fecha_egreso(self):
        fecha_egreso = self.cleaned_data.get('fecha_egreso')
        estado_en_hogar = self.cleaned_data.get('estado_en_hogar')

        if estado_en_hogar == 'E' and not fecha_egreso:
            raise forms.ValidationError("La fecha de egreso es requerida para residentes egresados.")

        return fecha_egreso

    def clean(self):
        cleaned_data = super().clean()
        estado_en_hogar = cleaned_data.get('estado_en_hogar')
        fecha_egreso = cleaned_data.get('fecha_egreso')

        if estado_en_hogar == 'I' and fecha_egreso:
            self.add_error('fecha_egreso', "No se debe especificar una fecha de egreso para residentes activos o ingresados.")

        return cleaned_data


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'compuesto', 'dosis']
        labels = {
            'nombre': 'Nombre',
            'compuesto': 'Compuesto',
            'dosis': 'Dosis',
        }


class PlanMedicacionForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = PlanMedicacion
        # all fields
        fields = ["residente", "fecha_inicio"]

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio < timezone.now().date():
            raise forms.ValidationError("La fecha de inicio debe ser posterior o igual a la fecha actual.")
        return fecha_inicio