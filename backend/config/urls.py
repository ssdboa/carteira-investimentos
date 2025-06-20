# backend/config/urls.py

from django.contrib import admin
from django.urls import path, include  # Garanta que 'include' está importado
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints de Autenticação
    # Inclui a nossa URL de registro, que ficará em /api/users/register/
    path('api/users/', include('apps.users.urls')),

    # Endpoints de Login e Refresh de Token (prontos da biblioteca simplejwt)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]