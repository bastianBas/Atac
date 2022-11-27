from django.contrib import admin
from django.urls import path
from Inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('empleados/', views.listadoEmpleados),
    path('agregarEmpleados/', views.agregarEmpleados),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado),
    path('actualizarEmpleado/<int:id>', views.actualizarEmpleado),
]
