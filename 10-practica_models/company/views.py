from django.shortcuts import render
from django.http import HttpResponse

def create(request):
    return HttpResponse('creando..')
