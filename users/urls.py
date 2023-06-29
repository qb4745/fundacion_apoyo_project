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
]
