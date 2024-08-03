from django.shortcuts import get_object_or_404, render, redirect
from .models import Tasks
from .forms import TasksForm
from django.contrib import messages
from django.db.models import Q

def index(request):
    search_query = request.GET.get('search', '')
    tasks = Tasks.objects.filter(
        Q(title__contains=search_query)
    )

    # Verificar si no se encontraron tareas
    if not tasks.exists():
        no_results_message = "No se encontraron coincidencias."
    else:
        no_results_message = None

    context = {
        'tasks': tasks,
        'no_results_message': no_results_message,
        'search_query': search_query  # Pasar la consulta de búsqueda al contexto
    }
    return render(request, 'tasks/index.html', context)

# ver tarea
def view(request, id):
    tasks = Tasks.objects.get(id=id)
    context = {
        'tasks' : tasks
    }
    return render(request, 'tasks/detail.html', context)


def edit(request, id):
    tasks = Tasks.objects.get(id=id)

    # para que al darle al boton de editar nos muestre el formulario lleno y poder editarlo
    if request.method == 'GET':
        form = TasksForm(instance=tasks)
        context = {
            'form' : form,
            'id' : id
        }
        return render(request, 'tasks/edit.html', context)

    # para que al editarlo y darle a guardar este guarde lo editado y sustituya al anterior
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        context = {
            'form' : form,
            'id' : id
        }
        messages.success(request, "La tarea se ha actualizado.")
        return render(request, 'tasks/edit.html', context)
    

def create(request):
    # para darle al boton añadir y crear el formulario
    if request.method == 'GET':
        form = TasksForm()
        context = {
            'form' : form
        }
        return render(request, 'tasks/create.html', context)
    
    # para crear y guardar la nueva tarea
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "La tarea ha sido creada.")
        return redirect('tasks_create')


def delete(request, id):
    return redirect('confirm_delete', id=id)


def confirm_delete(request, id):
    tasks = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        tasks.delete()
        messages.success(request, "La tarea ha sido eliminado.")
        return redirect('tasks')
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/confirm_delete.html', context)

