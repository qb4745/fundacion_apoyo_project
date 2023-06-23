from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Mandato


class MandatoForm(forms.ModelForm):
    class Meta:
        model = Mandato
        fields = ['numero_tarjeta', 'casa_comercial', 'monto']
        labels = {
            'numero_tarjeta': _('Número de tarjeta'),
            'casa_comercial': _('Nombre Casa Comercial'),
            'monto': _('Monto'),
        }