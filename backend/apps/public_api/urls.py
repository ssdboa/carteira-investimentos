# backend/apps/public_api/urls.py
from django.urls import path
from .views import teste_api_view

app_name = 'public_api' # Define um namespace para as URLs deste app

urlpatterns = [
    path('teste/', teste_api_view, name='teste_api'),
]