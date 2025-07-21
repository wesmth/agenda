import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
import django
from django.conf import settings


DJANGO_BASE_DIR = Path(__file__).parent.parent #Aqui pegamos o caminho da raiz
NUMBER_OF_OBJECTS = 1000

# Adiciona o diretório raiz do projeto à lista de caminhos de pesquisa de módulos do Python,
# permitindo importar módulos do projeto mesmo
sys.path.append(str(DJANGO_BASE_DIR))


# Define a variável de ambiente que indica ao Django qual arquivo de configurações usar.
os.environ['DJANGO_SETTINGS_MODULE']='project.settings'

#desativa o uso de timezones no Django, fazendo com que datas e horários sejam tratados como locais, não como UTC. Isso pode ser útil para evitar conversões automáticas de fuso horário ao manipular datas.
settings.USE_TZ = False 

django.setup() #inicializa o Django, carregando as configurações e preparando o ambiente para usar os recursos do framework, como modelos e consultas ao banco de dados.

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    #Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos','Família','Conhecidos','Trabalho']
    
    django_categories = [Category(name=name) for name in categories]

    

    for category in django_categories:
        category.save()

    django_contacts = []

    for n in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ',1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars = 100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                email = email,
                created_date = created_date,
                description = description,
                category=category,
            )
        )
    
    if len(django_contacts)>0:
        Contact.objects.bulk_create(django_contacts)
        print('Finalizado')