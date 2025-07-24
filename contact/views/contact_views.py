from django.shortcuts import render
from contact.models import Contact
# Importa a função 'render', que serve pra renderizar  um template HTML com contexto, se quiser

def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'contact/index.html',context)
