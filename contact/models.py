from django.db import models
from django.utils import timezone # importamos isso para sabermos a data atual

# id(primary key - automatico o proprio django cria)
# first_name (string) last_name(string)
# email (email), created_date(date) description (text)
# category (foreign key) show (boolean) owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    # para registrar uma pessoa, todos os campos abaixo são obrigatórios
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, blank=True)#colocando o blank, tiramos a obrigatoriedade do campo
    # a partir daqui não é mais obrigatório
    created_date = models.DateTimeField(default=timezone.now) #colocamos o timezone.now para que o django saiba que data o contato foi criado e assim o usuario não consegue editar esse campo manualmente.
    description = models.TextField(blank=True) #apesar de tanto o charfield quanto o textfield serem campos de texto/string, o charfield tem limitação de caracteres ja o textfield não.


    
