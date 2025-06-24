# backend/config/settings/base.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths...
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 2. Adicionar estas duas linhas para carregar o .env da raiz do projeto
# O .parent sobe um nível de diretório (de /backend para a raiz)
ENV_PATH = BASE_DIR.parent / '.env'
load_dotenv(dotenv_path=ENV_PATH)

# --- APLICAÇÕES E MIDDLEWARE ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Libs de terceiros
    'corsheaders',

    # Meus Apps
    'apps.public_api.apps.PublicApiConfig',
    'apps.users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Deve vir antes de CommonMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# --- BANCO DE DADOS (PADRÃO DE PRODUÇÃO) ---
# O ambiente de desenvolvimento irá sobrescrever esta configuração.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('MYSQL_PORT'),
    }
}


# --- VALIDAÇÃO DE SENHA ---

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- INTERNACIONALIZAÇÃO ---

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- ARQUIVOS ESTÁTICOS ---

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- CONFIGURAÇÕES DE CORS ---
# Carrega as configurações principais a partir das variáveis de ambiente

CORS_ALLOWED_ORIGINS_ENV = os.environ.get('CORS_ALLOWED_ORIGINS')
CORS_ALLOWED_ORIGINS = []
if CORS_ALLOWED_ORIGINS_ENV:
    CORS_ALLOWED_ORIGINS.extend([origin.strip() for origin in CORS_ALLOWED_ORIGINS_ENV.split(',') if origin.strip()])

CORS_ALLOWED_ORIGIN_REGEXES_ENV = os.environ.get('CORS_ALLOWED_ORIGIN_REGEXES')
CORS_ALLOWED_ORIGIN_REGEXES = []
if CORS_ALLOWED_ORIGIN_REGEXES_ENV:
    CORS_ALLOWED_ORIGIN_REGEXES.extend([origin.strip() for origin in CORS_ALLOWED_ORIGIN_REGEXES_ENV.split(',') if origin.strip()])
