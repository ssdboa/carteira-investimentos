# backend/config/settings/production.py

from .base import *

# --- CONFIGURAÇÕES DE PRODUÇÃO ---

DEBUG = False

# Em produção, a SECRET_KEY DEVE ser carregada do ambiente.
# Usar os.environ[...] em vez de .get() causa um erro se a variável não
# for definida, o que é uma falha de segurança importante.
SECRET_KEY = os.environ['SECRET_KEY']


# Em produção, ALLOWED_HOSTS DEVE ser carregado do ambiente.
ALLOWED_HOSTS_ENV = os.environ.get('DJANGO_ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_ENV.split(',') if host.strip()]
else:
    # Se não for definido, a lista fica vazia, e o Django não iniciará.
    # Isso é uma medida de segurança. Configure no Render!
    ALLOWED_HOSTS = []

# Nota: As configurações de DATABASES e CORS já estão prontas para produção
# no arquivo base.py, pois elas leem as variáveis de ambiente que você
# irá configurar no Render.