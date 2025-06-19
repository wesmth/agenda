"""
URL configuration for project project.

Esse arquivo define o mapeamento das URLs principais do projeto.
Ou seja, quando alguém acessa uma URL no navegador, é aqui que Django descobre qual view mostrar.

O `urlpatterns` é uma lista com todas as rotas do projeto.

Documentação: https://docs.djangoproject.com/en/5.2/topics/http/urls/

Tem 3 tipos de exemplo aqui:
- Function views (funções como views)
- Class-based views (views em forma de classe)
- URLconf de outro app (usar include pra importar rotas de outros apps)
"""

from django.contrib import admin

from django.urls import path, include
# path → pra definir rotas
# include → pra puxar as rotas de outro app 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
    # Quando acessar a raiz do site (/), vai buscar as rotas definidas no arquivo contact/urls.py
]
