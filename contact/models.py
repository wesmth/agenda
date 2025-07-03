from django.db import models
from django.utils import timezone  # Importa o timezone pra pegar a data e hora atual certinha

# Classe Contact representa um contato da agenda, tipo um cadastro de pessoa
class Contact(models.Model):
    # Campo obrigatório: primeiro nome da pessoa, com no máximo 35 caracteres
    first_name = models.CharField(max_length=35)

    # Campo obrigatório: sobrenome da pessoa, com no máximo 35 caracteres
    last_name = models.CharField(max_length=35)

    # Campo obrigatório: telefone (pode incluir DDD junto), no máximo 11 dígitos
    phone = models.CharField(max_length=11)

    # Campo opcional: email da pessoa, no máximo 50 caracteres. O 'blank=True' permite deixar esse campo vazio no formulário
    email = models.EmailField(max_length=50, blank=True)

    # Campo automático: armazena a data e hora de criação do contato
    # timezone.now garante que será a data/hora atual no momento da criação
    created_date = models.DateTimeField(default=timezone.now)

    # Campo opcional: descrição livre sobre a pessoa. Pode ser uma bio, observações etc.
    # TextField aceita textos longos, diferente do CharField
    description = models.TextField(blank=True)

    # Campo booleano: define se o contato vai ser exibido ou não (tipo "ativo" ou "inativo")
    show = models.BooleanField(default=True)

    # Campo opcional: imagem do contato. O upload_to define a pasta onde a imagem vai ser salva com base no ano e mês
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # Método que define como o objeto será representado quando for convertido em string
    # Assim, ao exibir no painel admin ou em outros lugares, mostra o nome completo em vez de "Contact object (1)"
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
