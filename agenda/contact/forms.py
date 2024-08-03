from django.forms import ModelForm
#from django import forms
from .models import Contact

# creando un modelform le colocamos el mismo nombre del models
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)
    
