# backend/apps/public_api/urls.py

from django.urls import path
from .views import public_api_status

urlpatterns = [
    path('status/', public_api_status, name='public_api_status'),
]