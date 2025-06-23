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
