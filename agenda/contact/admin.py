from django.contrib import admin
from .models import Contact

# para registrar el modelo y salga en el panel de admin
admin.site.register(Contact)
