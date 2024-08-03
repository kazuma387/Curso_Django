from django import forms 

# para crear el formulario
class CommentForm(forms.Form):
    name = forms.CharField(label='Escribe tu nombre', max_length=100, help_text='100 caracteres maximo')
    url = forms.URLField(label='Tú sitio web', required=False, initial='http://')
    comment = forms.CharField(label='comentarios')


# crear formulario de contacto y agregarle widget
class ContactForm(forms.Form):
    # con widget=forms.TextInput(attrs={'class':input}) le damos una clase y podremos darle estilos con css
    name = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class':'input_name'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class':'input_email'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class':'text_message'}))

    # validaciones personalizadas
    def clean_name(self):
        # obteniendo el valor de name despues de pasar las validaciones normales para aplicarles las personalizadas
        name = self.cleaned_data.get('name')
        # haciendo validaciones personalizadas
        if name == 'open':
            raise forms.ValidationError('Este campo no esta permitido')
        else:
            return name

