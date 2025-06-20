# backend/config/settings/development.py

from .base import *

# --- CONFIGURAÇÕES DE DESENVOLVIMENTO ---

DEBUG = True

# Chave secreta simples para ambiente local. Não use em produção!
SECRET_KEY = 'django-insecure-local-dev-key-change-me'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# A configuração de DATABASES que usava SQLite foi REMOVIDA.
# Agora, este arquivo herdará a configuração do MySQL definida em 'base.py'.

# --- CORS PARA DESENVOLVIMENTO ---
# Adiciona as URLs locais à lista de origens permitidas.

CORS_ALLOWED_ORIGINS.extend([
    "http://localhost:3000",
    "http://127.0.0.1:3000",
])