from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

def create(request):
    # art1 = Article(headLine='Articulo 1')
    # art1.save()
    # art2 = Article(headLine='Articulo 2')
    # art2.save()
    # art3 = Article(headLine='Articulo 3')
    # art3.save()

    # pub1 = Publication(title='Publicación 1')
    # pub1.save()
    # pub2 = Publication(title='Publicación 2')
    # pub2.save()
    # pub3 = Publication(title='Publicación 3')
    # pub3.save()
    # pub4 = Publication(title='Publicación 4')
    # pub4.save()
    # pub5 = Publication(title='Publicación 5')
    # pub5.save()
    # pub6 = Publication(title='Publicación 6')
    # pub6.save()
    # pub7 = Publication(title='Publicación 7')
    # pub7.save()

    # # para añadir la relacion manytomany 
    # art1.publications.add(pub1)
    # art1.publications.add(pub2)
    # art1.publications.add(pub3)
    # art2.publications.add(pub4)
    # art2.publications.add(pub5)
    # art3.publications.add(pub6)
    # art3.publications.add(pub7)

    # result = art1.publications.all()

    # para relacionar pub con art
    pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()

    # para eliminar la relacion de un art con un pub
    # art1.publications.remove(pub2)
    
    return HttpResponse(result)
