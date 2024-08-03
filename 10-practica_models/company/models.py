from django.db import models

# clase pais
class Country(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)
    
    def __str__(self):
        return self.name

# clase locacion
class Location(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    # relacion muchos a uno
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='location')
    
    def __str__(self):
        return self.name

# clase salario
class Salary(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    extra_jun = models.BooleanField(default=False)
    extra_dec = models.BooleanField(default=False)
    
    def __str__(self):
        return self.amount

# clase trabajo
class Job(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=255,null=True)
    # relacion muchos a uno
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, related_name='job')
    
    def __str__(self):
        return self.title

# clase lugar
class Place(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)
    # relacion muchos a uno
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='place')

    def __str__(self):
        return self.name
    
    # clase empleado
class Employee(models.Model):
    id_number = models.CharField(max_length=30, blank=False, null=False)
    name = models.CharField(max_length=80, blank=False, null=False)
    last_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # relacion muchos a uno
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='employee')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.id_number


