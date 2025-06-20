# backend/apps/users/urls.py

from django.urls import path
from .views import RegisterView

# Este urlpatterns será incluído no arquivo de urls principal do projeto
urlpatterns = [
    # Mapeia a rota 'register/' para a nossa RegisterView
    path('register/', RegisterView.as_view(), name='auth_register'),
]