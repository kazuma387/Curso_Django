from django.forms import ModelForm
from .models import Employee

# creando un modelform le colocamos el mismo nombre del models
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ("name", "last_name", "email")

        # tambien si queremos que pintar todos los elementos hay un atajo y es este
        fields = '__all__'

        # si quiero añadir un campo mas usamos
        #extra_fields = ('address')

        # si quiero escluir a uno o dos de todos uso
        #exclude = ('email',)

