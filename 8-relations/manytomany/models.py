from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    headLine = models.CharField(max_length=100)
    # para relacionarlo manytomany con publication
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headLine

