
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/formulario/', views.getFormulario, name='formulario'),
    path('get/meta/', views.getMeta, name='meta'),
    path('post/formulario/', views.postFormulario, name='postformulario'),
    path('post/meta/', views.postMeta, name='postmeta')
]
