from django.contrib import admin
from Inicio.models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'rut', 'correo', 'cargo', 'area']

admin.site.register(Empleado, EmpleadoAdmin)


