from django.forms import DateInput, ModelForm
from .models import Tasks

# creando un modelform le colocamos el mismo nombre del models
class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'estimated_end': DateInput(attrs={'type' : 'date'}),
            'date' : DateInput(attrs={'type' : 'date'}),
        }