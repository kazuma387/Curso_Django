# para trabajar las vistas
# son un conjunto de funciones las cuales siempre almenos tendrán un parametro 'request' que son las peticiones

from django.http import HttpResponse

# vista saludo
def saludo(request):
    return HttpResponse("Hola Mundo")

# vista despedida
def despedida(request):
    return HttpResponse("Hasta luego")

# vista ruta con parametros
def adulto(request, edad):
    if edad >= 18:
        return HttpResponse(f"Tienes {edad}, eres mayor de edad")
    else:
        return HttpResponse(f"Tienes {edad}, no eres mayor de edad")