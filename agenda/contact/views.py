from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.db.models import Q

def index(request, letter = None):
    # para buscar por la primera letra
    if letter != None:
        search_query = None
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        # para el buscador
        search_query = request.GET.get('search', '')
        contacts = Contact.objects.filter(
            Q(name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(mobile__contains=search_query) |
            Q(phone__contains=search_query)
        )

    # Verificar si no se encontraron contactos
    if not contacts.exists():
        no_results_message = "No se encontraron coincidencias."
    else:
        no_results_message = None

    if search_query == None:
        context = {
        'contacts': contacts,
        'no_results_message': no_results_message,
        }
    else:
        context = {
            'contacts': contacts,
            'no_results_message': no_results_message,
            'search_query': search_query  # Pasar la consulta de búsqueda al contexto
        }
    return render(request, 'contact/index.html', context)

# ver contacto
def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact' : contact
    }
    return render(request, 'contact/detail.html', context)


def edit(request, id):
    contact = Contact.objects.get(id=id)

    # para que al darle al boton de editar nos muestre el formulario lleno y poder editarlo
    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {
            'form' : form,
            'id' : id
        }
        return render(request, 'contact/edit.html', context)

    # para que al editarlo y darle a guardar este guarde lo editado y sustituya al anterior
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context = {
            'form' : form,
            'id' : id
        }
        messages.success(request, "El contacto de ha actualizado.")
        return render(request, 'contact/edit.html', context)
    

def create(request):
    # para darle al boton añadir y crear el formulario
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form' : form
        }
        return render(request, 'contact/create.html', context)
    
    # para crear y guardar el nuevo contacto
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "El contacto ha sido creado.")
        return redirect('contact_create')


def delete(request, id):
    return redirect('contact_confirm_delete', id=id)


def confirm_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "El contacto ha sido eliminado.")
        return redirect('contact')
    context = {
        'contact': contact
    }
    return render(request, 'contact/contact_confirm_delete.html', context)
