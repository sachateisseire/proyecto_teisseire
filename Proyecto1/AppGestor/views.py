from django.http import HttpResponse
from django.shortcuts import render
from AppGestor.models import Departamentos, Expedientes, Personal
from AppGestor.forms import DepartamentosFormulario, ExpedientesFormulario, PersonalFormulario

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

def departamentosFormulario(request):

    if request.method == 'POST':

        miFormulario = DepartamentosFormulario(request.POST)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            departamentos = Departamentos (reparticion=informacion['reparticion'])

            departamentos.save()
            
            return render(request, "AppGestor/departamentosFormulario.html")

    else:
        miFormulario = DepartamentosFormulario()
    
    return render(request, "AppGestor/departamentosFormulario.html", {"miFormulario":miFormulario})

def departamentosFormularioPost(request):

    print('------------------')
    print(request.post)

    mi_departamento = Departamentos(id='', reparticion=reparticion)
    mi_departamento.save()

    return render(request, 'AppGestor/departamentos.html', {'reparticion': reparticion})
    
    # return render(request, "AppGestor//inicio.html")

def personalFormulario(request):

    if request.method == 'POST':

        miFormulario = PersonalFormulario(request.POST)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            personal = Personal (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], categoria=informacion['categoria'], email=informacion['email'])

            personal.save()
            
            return render(request, "AppGestor/personalFormulario.html")

    else:
        miFormulario = PersonalFormulario()
    
    return render(request, "AppGestor/personalFormulario.html", {"miFormulario":miFormulario})

def expedientesFormulario(request):

    if request.method == 'POST':

        miFormulario = ExpedientesFormulario(request.POST)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            expedientes = Expedientes (numero=informacion['numero'], estado=informacion['estado'])

            expedientes.save()
            
            return render(request, "AppGestor/departamentosFormulario.html")

    else:
        miFormulario = ExpedientesFormulario()
    
    return render(request, "AppGestor/expedientesFormulario.html", {"miFormulario":miFormulario})
