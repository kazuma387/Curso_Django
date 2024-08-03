from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=800, null=True)
    date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name