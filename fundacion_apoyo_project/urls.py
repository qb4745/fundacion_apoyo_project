from django.contrib import admin
from django.urls import path
from django.urls import include

from core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='core-home'),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls', namespace='users')),
]
