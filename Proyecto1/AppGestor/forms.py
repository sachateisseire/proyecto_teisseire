from django import forms

class DepartamentosFormulario(forms.Form):

    reparticion = forms.CharField()

class PersonalFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    categoria = forms.CharField()
    email = forms.EmailField()

class ExpedientesFormulario(forms.Form):

    numero = forms.CharField()
    numero = forms.BooleanField()
    