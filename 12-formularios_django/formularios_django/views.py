from django.shortcuts import render
from django.http import HttpResponse
from.forms import CommentForm, ContactForm

# metodo get
def form(request):
    comment_form = CommentForm()
    return render(request, 'form.html', {'comment_form' : comment_form})

def goal(request):
    if request.method != 'GET':
        return HttpResponse('Error....')
    
    name = request.GET['name']
    return render(request, 'succes.html', {'name' : name})

# metodo post
def postform(request):
    comment_form = CommentForm()
    return render(request, 'postform.html', {'comment_form' : comment_form})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('Error....')
    
    name = request.POST['name']
    return render(request, 'succes.html', {'name' : name})

# para los widget y la vadilación del formulario
def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form' : form})
    
    # validando el formulario
    if request.method == 'POST':
        # creando form con los datos recividos de contactform
        form = ContactForm(request.POST)
        if form.is_valid():
            # aquí irian todas las acciones a realizar si los datos son corectos
            return HttpResponse('Valido')
        else:
            # aquí irian todas las acciones a realizar si los datos no son corectos
            return render(request, 'widget.html', {'form' : form})