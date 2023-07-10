from django.contrib import admin
from .models import Mandato, Residente, Fichamedica, Ingreso, Egreso, Medicamento, PlanMedicacion, DosisMedicamento
# Register your models here.



admin.site.register(Mandato)
admin.site.register(Residente)
admin.site.register(Fichamedica)
admin.site.register(Ingreso)
admin.site.register(Egreso)
admin.site.register(Medicamento)
admin.site.register(PlanMedicacion)
admin.site.register(DosisMedicamento)

