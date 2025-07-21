from django.db import models
from django.utils import timezone  # Importa o timezone pra garantir que a data/hora esteja correta com fuso e tudo
from django.contrib.auth.models import User
# Classe que representa uma categoria de contatos (tipo: Família, Amigos, Trabalho, etc.)
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'  # Define o nome amigável da classe no admin do Django

    name = models.CharField(max_length=50)  # Nome da categoria, tipo "Família", "Trampo"... até 50 caracteres

    def __str__(self):
        return self.name  # Quando aparecer essa categoria em algum lugar, vai exibir só o nome dela
        


# Classe que representa um contato da agenda (tipo uma fichinha de uma pessoa cadastrada)
class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'  # Nome que vai aparecer no admin

    # Primeiro nome da pessoa. Campo obrigatório. Limite de 35 caracteres.
    first_name = models.CharField(max_length=35)

    # Sobrenome da pessoa. Também obrigatório e com limite de 35 caracteres.
    last_name = models.CharField(max_length=35)

    # Telefone da pessoa. Pode incluir DDD. Máximo de 11 caracteres (ex: 41912345678).
    phone = models.CharField(max_length=11)

    # E-mail da pessoa. Não é obrigatório (por isso o blank=True). Máximo de 50 caracteres.
    email = models.EmailField(max_length=50, blank=True)

    # Data/hora em que o contato foi criado. Usa o timezone.now pra garantir o horário certo.
    created_date = models.DateTimeField(default=timezone.now)

    # Campo de texto livre pra colocar uma descrição, observações, anotações ou o que quiser.
    # Pode deixar vazio (blank=True) e aceita texto grande.
    description = models.TextField(blank=True)

    # Campo que define se o contato vai ser exibido ou não na lista. Útil pra "arquivar" contato sem apagar.
    show = models.BooleanField(default=True)

    # Campo pra salvar uma imagem do contato (foto de perfil). 
    # blank=True permite deixar vazio, e upload_to define a pasta onde vai ser salva (organizada por ano e mês).
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # Categoria do contato. É uma relação com a tabela Category.
    # Pode ser deixado em branco e nulo (blank=True, null=True).
    # Se a categoria for apagada, esse campo vira NULL (por causa do on_delete=models.SET_NULL).
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True
    )

    # Define como o contato vai aparecer em representações de texto, como no admin ou no terminal.
    # Em vez de "Contact object (1)", vai mostrar tipo "Maria Silva".
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


