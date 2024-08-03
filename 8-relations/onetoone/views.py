from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurtant

# Create your views here.
def create(request):
    # cramos un objeto place y lo salvamos
    place = Place(name='name 1', address='calle 1')
    place.save()

    # creamos un objeto restaurant y le asociamos el place
    restaurant = Restaurtant(place=place, number_of_employees=5)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
