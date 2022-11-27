from django.shortcuts import render,redirect
from Inicio.forms import FormEmpleado
from Inicio.models import Empleado
from . import forms

def index(request):
    return render(request, 'Inicio/index.html')

def listadoEmpleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'Inicio/empleados.html', data)

def agregarEmpleados(request):
    form = FormEmpleado()
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Inicio/agregarEmpleados.html', data)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    return redirect('/empleados',)

def actualizarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    form = FormEmpleado(instance=empleado)
    if request.method == 'POST':
        form = FormEmpleado(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Inicio/agregarEmpleados.html', data)
