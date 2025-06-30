# Importando o módulo de administração do Django
from django.contrib import admin

# Importando o modelo Contact que está na app 'contact'
from contact.models import Contact

# Decorador que registra a classe ContactAdmin como a responsável
# por configurar a exibição do modelo Contact no painel administrativo do Django
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Define os campos que vão aparecer na listagem de contatos no admin
    list_display = ('first_name', 'last_name', 'phone', 'email')
    
    # Define a ordenação padrão da listagem (aqui, por nome em ordem crescente)
    ordering = ('id',)

    # Cria um filtro lateral com base no campo 'created_date'
    # Útil pra filtrar os contatos por data de criação
    list_filter = ('created_date',)

    # Adiciona uma barra de busca no admin, permitindo procurar por nome e sobrenome
    search_fields = ('first_name', 'last_name')

    # Define quantos itens vão aparecer por página na listagem
    list_per_page = 20

    # Define o máximo de itens que podem ser exibidos quando clicar em "Mostrar tudo"
    list_max_show_all = 100
