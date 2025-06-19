from django.shortcuts import render
# Importa a função 'render', que serve pra renderizar  um template HTML com contexto, se quiser

def index(request):
    return render(request, 'contact/index.html',)
    # Retorna a resposta renderizada do template 'contact/index.html'
    # O terceiro argumento (contexto) está vazio por enquanto, mas pode ser usado pra passar dados pro HTML
