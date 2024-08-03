from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.first_name

class Article(models.Model):
    head_line = models.CharField(max_length=100)
    pub_date = models.DateField()
    # para asociar cada uno de los articles con un reporter
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, related_name='articles')


    def __str__(self):
        return self.head_line
