from django.urls import path, include
# Importa as funções 'path' (pra criar rotas/URLs) e 'include' (caso tu queira importar URLs de outros apps depois)

from contact import views
# Importa o módulo de views do app 'contact', onde tá a função que vai responder à URL

urlpatterns = [
    path('', views.index, name='index'),
    # Define uma rota raiz ('/') que chama a view 'index' do app 'contact'
    # name='index' serve pra usar essa URL em templates e redirecionamentos pelo nome
]
