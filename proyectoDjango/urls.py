"""proyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appDjango.views import mostrar_familiares, BuscarFamiliar, ActualizarFamiliar, AltaFamiliar, BorrarFamiliar, mostrar_mascotas, AltaMascota, ActualizarMascota, BuscarMascota, BorrarMascota, mostrar_vehiculos, BuscarVehiculo, AltaVehiculo, ActualizarVehiculo, BorrarVehiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscarFamiliar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-mascotas/', mostrar_mascotas),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mis-mascotas/buscarMascota', BuscarMascota.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    path('vehiculos/', mostrar_vehiculos),
    path('vehiculos/buscarVehiculo', BuscarVehiculo.as_view()),
    path('vehiculos/alta', AltaVehiculo.as_view()),
    path('vehiculos/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('vehiculos/borrar/<int:pk>', BorrarVehiculo.as_view()),
]
