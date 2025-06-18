# Iniciar o projeto Django

```
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install django
django-admin startproject project . # o ponto final serve para colocar os arquivos de configuração direto na raiz do projeto.
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
```