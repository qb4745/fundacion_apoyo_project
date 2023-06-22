from django.urls import path
from .views import (DashBoardView)

app_name = 'users'

urlpatterns = [
    path('', DashBoardView.as_view(), name='users-dashboard'),
]
