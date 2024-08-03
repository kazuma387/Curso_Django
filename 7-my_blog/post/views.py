from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

# Create your views here.
def queries(request):
    # consula, obtener todos los elementos
    authors = Author.objects.all()

    # obtener datos filtrados por condición
    filtered = Author.objects.filter(email='james62@example.com')

    # obtener un unico elemento (filtrado)
    author = Author.objects.get(id=5)

    # consula, obtener los 10 primeros elementos
    limit = Author.objects.all()[:10]

    # consula, obtener 10 elementos saltando los 40 primeros
    offset = Author.objects.all()[5:10]

    # consula, ordenar todos los elementos
    orders = Author.objects.all().order_by('email')

    # obtener elementos cuyo id sea mayor o igual a 10 y menor o igual a 20(filtrado)
    # __lte = menor o igual que, __gte= mayor o igual que, __lt= menor que, __gt= mayor que, contains= contiene, __exact= exacto
    filtered2 = Author.objects.filter(id__gte=10, id__lte=20)

    # obtener elementos que contengan la palabra play(filtrado)
    filtered3 = Author.objects.filter(name__contains='play')

    return render(request, 'post/queries.html', 
    {'authors' : authors, 'filtered' : filtered, 'author' : author,
        'limit' : limit, 'offset' : offset, 'orders' : orders, 'filtered2' : filtered2,'filtered3' : filtered3 })

# actualizando datos
def update(request):
    author = Author.objects.get(id=1)
    author.name = 'Daniel Rios'
    author.email = 'Touma387@gmail.com'
    author.save()
    return HttpResponse('actualizando..')
