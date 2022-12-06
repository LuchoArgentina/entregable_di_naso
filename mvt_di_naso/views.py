from django.http import HttpResponse 
from django.template import Template, Context
from AppFamilia.views import *

def inicio(request):
    return HttpResponse("Programa web - Listado de familiares")

def mostrarHtml(request):
    
    familiares={"nombre1":"Angela","apellido1":"Saccone","dni1":1254582,"fecha_nacimiento1":"1920-12-07","parentesco1":"Abuela",
    "nombre2":"Salvador","apellido2":"Di Naso","dni2":4254582, "fecha_nacimiento2":"1922-06-22","parentesco2":"Abuelo",
    "nombre3":"Franco","apellido3":"Di Naso","dni3":13425785, "fecha_nacimiento3":"1952-05-01","parentesco3":"Tio"}
    archivo=open("D:/Python_Coder/entregable/mvt_di_naso/Plantillas/Template1.html")
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(familiares)
    documento=template.render(contexto) #Completa los espacios vacios con los datos de mi contexto
    
    return HttpResponse(documento)