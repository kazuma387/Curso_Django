from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasks'),
    path('view/<int:id>', views.view, name='tasks_view'),
    path('edit/<int:id>', views.edit, name='tasks_edit'),
    path('create/', views.create, name='tasks_create'),
    path('delete/<int:id>', views.delete, name='tasks_delete'),
    path('confirm_delete/<int:id>/', views.confirm_delete, name='confirm_delete')
]