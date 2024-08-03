from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='kazuma', last_name='satou', email='kazuma5962@gmail.com')
    rep.save()

    art_1 = Article(head_line='sekaisubarachi temporada 1', pub_date=date(2016,3,16), reporter=rep)
    art_1.save()

    art_2 = Article(head_line='sekaisubarachi temporada 2', pub_date=date(2017,3,16), reporter=rep)
    art_2.save()

    art_3 = Article(head_line='sekaisubarachi temporada 3', pub_date=date(2024,4,10), reporter=rep)
    art_3.save()

    # del articulo al reportero
    result = art_1.reporter.first_name

    # del reportero ver todos sus articulos
    #result2 = rep.articles.all()

    # ver numero de articulos
    result2 = rep.articles.count()

    return HttpResponse(result2)


