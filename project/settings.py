"""
Django settings for project project.

Esse arquivo contém todas as configurações do projeto Django.
Inclui desde apps instalados, banco de dados, até configuração de arquivos estáticos.

Documentação:
https://docs.djangoproject.com/en/5.2/topics/settings/
"""

from pathlib import Path  # Biblioteca pra trabalhar com caminhos de arquivos

# BASE_DIR representa o diretório base do projeto
# Ex: /home/seuusuario/seuprojeto
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# SEGURANÇA E DEBUG
# ========================

# Chave secreta usada pra criptografar dados. Nunca compartilhe isso num projeto real!
SECRET_KEY = 'django-insecure-zkymwah-wqmbvvj2hh3+_t#%6pv57nhh&mp#6$-b&b&0jrlk_k'

# DEBUG True mostra erros detalhados no navegador. Nunca usar em produção!
DEBUG = True

# Lista de domínios que podem acessar o site. Em produção, deve incluir o domínio real.
ALLOWED_HOSTS = []

# ========================
# APLICATIVOS INSTALADOS
# ========================

INSTALLED_APPS = [
    'django.contrib.admin',          # Painel admin
    'django.contrib.auth',           # Autenticação
    'django.contrib.contenttypes',   # Tipo de conteúdo dos models
    'django.contrib.sessions',       # Sessões (cookies, login)
    'django.contrib.messages',       # Mensagens de feedback
    'django.contrib.staticfiles',    # Arquivos estáticos (CSS, JS, imagens)

    # App do projeto
    'contact',  # App criado pra gerenciar contatos
]

# ========================
# MIDDLEWARES
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Segurança básica
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerencia sessões
    'django.middleware.common.CommonMiddleware',  # Coisas comuns como redirects
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra CSRF (ataques maliciosos)
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Feedback de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# ========================
# URLS E TEMPLATES
# ========================

# Aponta pro arquivo de rotas principal do projeto
ROOT_URLCONF = 'project.urls'

# Configuração dos templates HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Usa o sistema de templates do Django
        'DIRS': [ BASE_DIR / 'base_templates' ],  # Pasta onde ficam os templates principais
        'APP_DIRS': True,  # Django também vai procurar templates nas pastas dos apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # Permite acessar o request nos templates
                'django.contrib.auth.context_processors.auth',  # Permite usar info do usuário autenticado
                'django.contrib.messages.context_processors.messages',  # Permite mostrar mensagens de feedback
            ],
        },
    },
]

# Aponta pro arquivo WSGI (interface entre servidor web e Django)
WSGI_APPLICATION = 'project.wsgi.application'

# ========================
# BANCO DE DADOS
# ========================

# Banco de dados padrão: SQLite (leve e fácil)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Usa SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Caminho pro arquivo do banco
    }
}

# ========================
# VALIDAÇÃO DE SENHA
# ========================

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },  # Evita senhas parecidas com nome/email do usuário
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },  # Tamanho mínimo
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },  # Evita senhas comuns
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },  # Evita senhas só com números
]

# ========================
# INTERNACIONALIZAÇÃO
# ========================

LANGUAGE_CODE = 'pt-br'  # Idioma padrão do projeto

TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário de São Paulo

USE_I18N = True  # Habilita internacionalização (traduções)

USE_TZ = True  # Usa o sistema de timezone do Django

# ========================
# ARQUIVOS ESTÁTICOS E MÍDIA
# ========================

# URL base pra acessar arquivos estáticos (CSS, JS)
STATIC_URL = 'static/'

# Pastas adicionais onde o Django vai procurar arquivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]

# Pasta final onde os arquivos estáticos serão reunidos após rodar o `collectstatic`
STATIC_ROOT = BASE_DIR / 'static'

# Configuração de arquivos de mídia (uploads, imagens etc)
MEDIA_URL = 'media/'  # URL base para acessar os arquivos
MEDIA_ROOT = BASE_DIR / 'media'  # Caminho onde os arquivos enviados vão ser salvos

# ========================
# CHAVE PRIMÁRIA PADRÃO
# ========================

# Define o tipo padrão para IDs dos models (usa BigAutoField = inteiro grandão)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


try:
    from project.local_settings import *
except ImportError:
    ...