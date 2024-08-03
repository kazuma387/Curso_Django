from datetime import date
from django.db import models

# clase para crear tabla del autor
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

# clase para crear tabla de lo que publica el autor
class Entry(models.Model):
    # el foreignKey es para vincular estas dos clases, la clases autor con la clase entry
    # el on_delete=models.CASCADE es par que cuando el author se borre las entradas asociadas con el tambien
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


