from django.urls import path

from .views import Departamentos, buscador, ingresar, inicio

urlpatterns = [

    path('', inicio),
    path('test/', Departamentos),
    path('ingresar/', ingresar),
    path('buscador/', buscador),
]