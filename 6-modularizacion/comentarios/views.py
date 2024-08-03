from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('Funciona correctamente')

def create(request):
    # comment = Comment(name='John', score=5, comment='Hola esto es un comentario')
    # comment.save()
    comment = Comment.objects.create(name='alex', score=8, comment='Hola esto es otro comentario')

    return HttpResponse('Probando la creación')

def delete(request):
    # comment = Comment.objects.get(id=1)
    # comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse('Probando los borrados')