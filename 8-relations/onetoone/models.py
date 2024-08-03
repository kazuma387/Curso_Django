from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurtant(models.Model):
    # estableser la relacion uno a uno con la clase Place
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employees = models.IntegerField(default=1)

    def __str__(self):
        return self.place.name



