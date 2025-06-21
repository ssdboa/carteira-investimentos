# backend/apps/users/views.py

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer

# CreateAPIView é uma view genérica do DRF que já nos dá a funcionalidade
# de 'POST' para criar um novo objeto. Nós só precisamos configurá-la.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Permite que qualquer usuário (mesmo não autenticado) acesse este endpoint.
    # crucial para uma tela de registro!
    permission_classes = (permissions.AllowAny,)
    # Diz à view qual 'tradutor' (Serializer) ela deve usar para validar e criar o usuário.
    serializer_class = UserSerializer