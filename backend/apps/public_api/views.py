# backend/apps/public_api/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer  # Importe o JSONRenderer
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])  # <-- ADICIONE ESTA LINHA
def public_api_status(request):
    """
    Um endpoint simples para verificar se a API pública está online.
    """
    return Response({"message": "API Pública conectada com sucesso!"}, status=status.HTTP_200_OK)