from django.urls import path
from .views import (DashBoardView,
                    MandatoView,
                    MandatoCreateView,
                    MandatoUpdateView,
                    MandatoDeleteView,
                    )

app_name = 'users'

urlpatterns = [
    path('', DashBoardView.as_view(), name='users-dashboard'),
    path('mandato/', MandatoView.as_view(), name='users-mandato'),
    path('mandato/create', MandatoCreateView.as_view(), name='users-mandato-create'),
    path('mandato/update/<int:pk>/', MandatoUpdateView.as_view(), name='users-mandato-update'),
    path('mandato/delete/<int:pk>/', MandatoDeleteView.as_view(), name='users-mandato-delete'),
]
