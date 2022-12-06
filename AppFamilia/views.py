from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

# Create your views here.


def familiar(request):
    familiar1=Familiar(nombre="Angela",apellido="Saccone",dni=1254582, fecha_nacimiento="1920-12-07",parentesco="Abuela")
    familiar1.save()
    familiar2=Familiar(nombre="Salvador",apellido="Di Naso",dni=4254582, fecha_nacimiento="1922-06-22",parentesco="Abuelo")
    familiar2.save()
    familiar3=Familiar(nombre="Franco",apellido="Di Naso",dni=13425785, fecha_nacimiento="1952-05-01",parentesco="Tio")
    familiar3.save()
    cadena_texto=f"*******FAMILIAR NRO 1 *******- Nombre: {familiar1.nombre} , Apellido: {familiar1.apellido}, DNI: {familiar1.dni}, Nacimiento: {familiar1.fecha_nacimiento}, Parentesco: {familiar1.parentesco} *******FAMILIAR NRO 2 ******* Nombre: {familiar2.nombre} , Apellido: {familiar2.apellido}, DNI: {familiar2.dni},  Nacimiento: {familiar2.fecha_nacimiento}, Parentesco: {familiar2.parentesco} *******FAMILIAR NRO 3 ******* Nombre: {familiar3.nombre} , Apellido: {familiar3.apellido}, DNI: {familiar3.dni},  Nacimiento: {familiar3.fecha_nacimiento}, Parentesco: {familiar3.parentesco}"
    return HttpResponse(cadena_texto)