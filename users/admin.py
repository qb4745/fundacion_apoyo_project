from django.contrib import admin
from .models import Mandato, Residente, Fichamedica
# Register your models here.

admin.site.register(Mandato)
admin.site.register(Residente)
admin.site.register(Fichamedica)