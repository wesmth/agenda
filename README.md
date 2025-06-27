# Iniciar o projeto Django

```
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install django
django-admin startproject project . # o ponto final serve para colocar os arquivos de configuração direto na raiz do projeto.
python manage.py startapp contact
```

# Configurar o Git

```
git config --global user.name 'Seu nome'
git config --global user.email 'Seu email'
git config --global init.defaultBranch main
# configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
# cria o repositorio no github
git remote add origin COLA_LINK_DO_REPOSITORIO
git push -u origin main
```

# Migrando a base de dados

```
python manage.py makemigrations # como as migrations já estão criadas, você pode ignorar essa linha
python manage.py migrate
```

# Criando e modificando a senha de um super usuário Django

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

# Criando as models

```
# No arquivo models.py do app contact, criamos a seguinte model

class Contact(models.Model):
    # para registrar uma pessoa, todos os campos abaixo são obrigatórios
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, blank=True)#colocando o blank, tiramos a obrigatoriedade do campo
    # a partir daqui não é mais obrigatório
    created_date = models.DateTimeField(default=timezone.now) #colocamos o timezone.now para que o django saiba que data o contato foi criado e assim o usuario não consegue editar esse campo manualmente.
    description = models.TextField(blank=True) #apesar de tanto o charfield quanto o textfield serem campos de texto/string, o charfield tem limitação de caracteres ja o textfield não.

    # Depois de criada, rodamos no terminal:
    python manage.py makemigrations # Cria as migrações
    python manage.py migrate # Migra
``` 