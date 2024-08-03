from django.forms import ModelForm
from .models import Product

# creando un modelform le colocamos el mismo nombre del models
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'