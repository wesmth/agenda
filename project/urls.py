"""
URL configuration for project project.

Esse arquivo define o mapeamento das URLs principais do projeto.
Ou seja, quando alguém acessa uma URL no navegador, é aqui que o Django descobre qual view mostrar.

O `urlpatterns` é uma lista com todas as rotas do projeto.

Documentação oficial: https://docs.djangoproject.com/en/5.2/topics/http/urls/

Tipos de exemplo aqui:
- Function views → views feitas como funções
- Class-based views → views feitas como classes
- URLconf de outro app → usando `include()` pra puxar as rotas de um app separado (como o app 'contact')
"""

from django.contrib import admin  # Importa o painel administrativo do Django
from django.conf.urls.static import static  # Pra servir arquivos estáticos durante o desenvolvimento
from django.urls import path, include  # path = define rotas | include = importa rotas de outros apps
from django.conf import settings  # Pega configurações do settings.py

# Lista com todas as rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota do painel de administração: /admin
    path('', include('contact.urls')),  # Rota principal: se alguém acessar '/', ele vai olhar pro arquivo contact/urls.py
]

# Adiciona configurações pra servir arquivos de mídia (imagens, etc) durante o modo de desenvolvimento
# MEDIA_URL = o prefixo da URL (ex: /media/)
# MEDIA_ROOT = onde os arquivos estão salvos no sistema de arquivos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
