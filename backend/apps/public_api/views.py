# backend/apps/public_api/views.py
from django.http import JsonResponse

def teste_api_view(request):
    """
    Uma view de teste simples para a public_api.
    """
    return JsonResponse({"message": "Olá da public_api do Django!"})