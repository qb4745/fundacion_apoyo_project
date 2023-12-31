from django.urls import path
from .views import (DashBoardView,
                    MandatoView,
                    MandatoCreateView,
                    MandatoUpdateView,
                    MandatoDeleteView,
                    ResidenteListView,
                    ResidenteCreateView,
                    ResidenteUpdateView,
                    ResidenteDeleteView,
                    ResidenteDetailView,
                    ResidenteIngresoEgresoListView,
                    ResidenteIngresoEgresoUpdateView,
                    MedicamentoListView,
                    MedicamentoCreateView,
                    MedicamentoUpdateView,
                    MedicamentoDeleteView,
                    PlanMedicacionListView,
                    PlanMedicacionCreateView,
                    PlanMedicacionUpdateView,
                    PlanMedicacionDeleteView,
                    PlanMedicacionDetailView,
                    DosisMedicamentoListView,
                    DosisMedicamentoCreateView,
                    DosisMedicamentoUpdateView,
                    DosisMedicamentoDeleteView,
                    DosisMedicamentoResidenteCreateView,
                    FichaMedicaListView,
                    FichaMedicaCreateView,
                    FichaMedicaUpdateView,
                    FichaMedicaDeleteView,
                    FichaMedicaDetailView,




                    )

app_name = 'users'

urlpatterns = [
    path('', DashBoardView.as_view(), name='users-dashboard'),
    path('mandato/', MandatoView.as_view(), name='users-mandato'),
    path('mandato/create', MandatoCreateView.as_view(), name='users-mandato-create'),
    path('mandato/update/<int:pk>/', MandatoUpdateView.as_view(), name='users-mandato-update'),
    path('mandato/delete/<int:pk>/', MandatoDeleteView.as_view(), name='users-mandato-delete'),
    path('residente/', ResidenteListView.as_view(), name='users-residente-list'),
    path('residente/create', ResidenteCreateView.as_view(), name='users-residente-create'),
    path('residente/update/<int:pk>/', ResidenteUpdateView.as_view(), name='users-residente-update'),
    path('residente/delete/<int:pk>/', ResidenteDeleteView.as_view(), name='users-residente-delete'),
    path('residente/details/<int:pk>/', ResidenteDetailView.as_view(), name='users-residente-detail'),
    path('residente/ingreso-egreso/', ResidenteIngresoEgresoListView.as_view(), name='users-residente-ingreso-egreso-list'),
    path('residente/ingreso-egreso/update/<int:pk>/', ResidenteIngresoEgresoUpdateView.as_view(), name='users-residente-ingreso-egreso-update'),
    path('medicamento/', MedicamentoListView.as_view(), name='users-medicamento-list'),
    path('medicamento/create', MedicamentoCreateView.as_view(), name='users-medicamento-create'),
    path('medicamento/update/<int:pk>/', MedicamentoUpdateView.as_view(), name='users-medicamento-update'),
    path('medicamento/delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='users-medicamento-delete'),
    path('planmedicacion/', PlanMedicacionListView.as_view(), name='users-planmedicacion-list'),
    path('planmedicacion/create', PlanMedicacionCreateView.as_view(), name='users-planmedicacion-create'),
    path('planmedicacion/update/<int:pk>/', PlanMedicacionUpdateView.as_view(), name='users-planmedicacion-update'),
    path('planmedicacion/delete/<int:pk>/', PlanMedicacionDeleteView.as_view(), name='users-planmedicacion-delete'),
    path('dosismedicamento/', DosisMedicamentoListView.as_view(), name='users-dosismedicamento-list'),
    path('dosismedicamento/create', DosisMedicamentoCreateView.as_view(), name='users-dosismedicamento-create'),
    path('dosismedicamento/update/<int:pk>/', DosisMedicamentoUpdateView.as_view(), name='users-dosismedicamento-update'),
    path('dosismedicamento/delete/<int:pk>/', DosisMedicamentoDeleteView.as_view(), name='users-dosismedicamento-delete'),
    path('planmedicacion/details/<int:pk>/', PlanMedicacionDetailView.as_view(), name='users-planmedicacion-detail'),
    path('planmedicacion/details/<int:pk>/dosismedicamentoresidente/create/', DosisMedicamentoResidenteCreateView.as_view(), name='users-dosismedicamentoresidente-create'),
    path('fichamedica/', FichaMedicaListView.as_view(), name='users-fichamedica-list'),
    path('fichamedica/create', FichaMedicaCreateView.as_view(), name='users-fichamedica-create'),
    path('fichamedica/update/<int:pk>/', FichaMedicaUpdateView.as_view(), name='users-fichamedica-update'),
    path('fichamedica/delete/<int:pk>/', FichaMedicaDeleteView.as_view(), name='users-fichamedica-delete'),
    path('fichamedica/details/<int:pk>/', FichaMedicaDetailView.as_view(), name='users-fichamedica-detail'),
]