# Importando o módulo de administração do Django
from django.contrib import admin

# Importando o modelo Contact que está na app 'contact'
from contact.models import Contact,Category


# Decorador que registra a classe ContactAdmin como responsável
# por configurar a exibição do modelo Contact no painel administrativo do Django
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na listagem de contatos do painel admin
    # Isso facilita a visualização direta dos dados mais importantes
    list_display = ('first_name', 'last_name', 'phone', 'email','category')

    # Define a ordenação padrão da lista de contatos
    # Nesse caso, ordena por ID (ordem de criação)
    ordering = ('id',)

    # Adiciona um filtro lateral no painel com base na data de criação do contato
    # Muito útil pra filtrar contatos por data, tipo "só os de hoje", "desta semana" etc.
    list_filter = ('created_date',)

    # Adiciona um campo de busca na parte superior da lista de contatos
    # O admin poderá pesquisar por nome e sobrenome
    search_fields = ('first_name', 'last_name')

    # Define o número de itens por página na listagem de contatos
    # Evita carregar tudo de uma vez, o que ajuda no desempenho
    list_per_page = 50

    # Define o número máximo de itens que podem ser mostrados de uma vez se clicar em "Mostrar tudo"
    list_max_show_all = 100


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)
