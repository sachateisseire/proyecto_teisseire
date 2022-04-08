from django import views
from django.urls import path
from AppGestor import views

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('test/', views.Departamentos),
    path('ingresar/', views.ingresar, name="Ingresar"),
    path('buscador/',  views.buscador, name="Buscador"),
    path('departamentosFormulario', views.departamentosFormulario, name="departamentosFormulario"),
    path('personalFormulario', views.personalFormulario, name="personalFormulario"),
    path('expedientesFormulario', views.expedientesFormulario, name="expedientesFormulario"),
    path('departamentos', views.departamentos, name="departamentos"),
    path('personal', views.personal, name="personal"),
    path('expedientes', views.expedientes, name="expedientes"),

]

