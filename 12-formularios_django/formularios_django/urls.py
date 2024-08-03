from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('goal/', views.goal, name='goal'),
    path('post/form/', views.postform, name='postform'),
    path('post/goal/', views.postgoal, name='postgoal'),
    path('widget/', views.widget, name='widget')
]
