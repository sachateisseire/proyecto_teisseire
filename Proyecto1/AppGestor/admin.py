from django.contrib import admin
from .models import Departamentos, Personal, Expedientes

# Register your models here.

admin.site.register(Departamentos)

admin.site.register(Personal)

admin.site.register(Expedientes)
