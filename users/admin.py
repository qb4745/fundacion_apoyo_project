from django.contrib import admin
from .models import Mandato, Residente, FichaMedica, Medicamento, PlanMedicacion, DosisMedicamento
# Register your models here.



admin.site.register(Mandato)
admin.site.register(Residente)
admin.site.register(FichaMedica)
admin.site.register(Medicamento)
admin.site.register(PlanMedicacion)
admin.site.register(DosisMedicamento)

