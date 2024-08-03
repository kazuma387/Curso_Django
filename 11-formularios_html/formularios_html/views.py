from django.shortcuts import render
from django.http import HttpResponse

# metodo get
def getFormulario(request):
    return render(request, 'formulario.html', {})

def getMeta(request):
    if request.method != 'GET':
        return HttpResponse('Error....')
    
    name = request.GET['introducir_nombre']
    return render(request, 'acces.html', {'name' : name})
        
# metodo post
def postFormulario(request):
    return render(request, 'postformulario.html', {})

def postMeta(request):
    if request.method != 'POST':
        return HttpResponse('Error....')
    
    name = request.POST['introducir_nombre']
    return render(request, 'postacces.html', {'name' : name})
        