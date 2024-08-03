from django.contrib import admin
from .models import Tasks

# para registrar el modelo y salga en el panel de admin
admin.site.register(Tasks)
