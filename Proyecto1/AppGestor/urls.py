from django import views
from django.urls import path

from .views import Departamentos, buscador, departamentosFormulario, ingresar, inicio

urlpatterns = [

    path('', inicio, name="Inicio"),
    path('test/', Departamentos),
    path('ingresar/', ingresar, name="Ingresar"),
    path('buscador/',  buscador, name="Buscador"),
    path('departamentosFormulario', departamentosFormulario, name="departamentosFormulario")

]

