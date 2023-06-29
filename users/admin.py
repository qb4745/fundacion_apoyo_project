from django.contrib import admin
from .models import Mandato, Residente, Fichamedica, Ingreso, Egreso
# Register your models here.



admin.site.register(Mandato)
admin.site.register(Residente)
admin.site.register(Fichamedica)
admin.site.register(Ingreso)
admin.site.register(Egreso)
