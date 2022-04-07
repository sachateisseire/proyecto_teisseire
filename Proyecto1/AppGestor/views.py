from django.http import HttpResponse
from django.shortcuts import render
from AppGestor.models import Departamentos

# Create your views here.

# def departamentos(self):

#     departamentos = Departamentos(reparticion="Administracion")
#     departamentos.save()

#     documentoDeTexto = f'Bien hecho'

#     return HttpResponse (documentoDeTexto)

def inicio(request):
    return render(request, 'AppGestor/inicio.html' )

def ingresar(request):
    return render(request, 'AppGestor/ingresar.html' )

def buscador(request):
    return render(request, 'AppGestor/buscador.html' )

def departamentos(self):
    return HttpResponse ('vista departamentos')

def personal(self):
    return HttpResponse ('vista personal')

def expedientes(self):
    return HttpResponse ('vista expedientes')
