from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from datetime import date
import os
from .models import Reporte,Area
from . import metodos

# Create your views here.

urlBase="reporteria/contenido/"

def valLogin(request):
    if not request.user.is_authenticated:
        if request.method != "POST":
            return render(request,urlBase+'login.html')
        else:
            usuario = request.POST["ususarioLog"]
            contrasena = request.POST["contrasenaLog"]
            user=authenticate(username=usuario,password=contrasena)
            if (user):
                print('Usuario de reporteria encontrado ',user)
                login(request,user)
                return redirect(to='home')
            else:
                print('Usuario no pertenece a reporteria')
                context={
                    'e_login':usuario
                }
                return render(request,urlBase+'login.html',context)
    else:
        return redirect(to='home')
    
def logOutReport(request):
    logout(request)
    return redirect(to='home')

def reporte(request):
    if request.user.is_authenticated:
        context={
            'reportes':Reporte.objects.all(),
            'areas': Area.objects.all(),
        }
        return render(request,urlBase+'reporte.html',context)
    else:
        return redirect(to="login")

def eliminarRt(request,pk):
    if request.user.is_superuser:
        objReporte=Reporte.objects.get(id=pk)
        objReporte.delete()
        return redirect('home')
    else:
        return redirect('login')
    
def modificarRt(request):
    if request.method !="POST":
        return redirect(to="home")
    else:
        id = request.POST["u-idRt"]
        razon = request.POST["u-razonRt"]
        id_area = request.POST["u-id_areaRt"]
        ObjArea=Area.objects.get(id_area=id_area)
        fecha_json = request.POST["u-fecha_DatosRt"]
        objReporte = Reporte.objects.get(id=id)
        if request.FILES.get("u-reporteRt"):
            reporte = request.FILES.get("u-reporteRt")
            objReporte.reporte = reporte
        objReporte.razon = razon
        objReporte.id_area = ObjArea
        objReporte.fecha_json = fecha_json
        
        objReporte.save()
        return redirect(to="home")

def dashboard(request):
    if request.user.is_authenticated:
        reportes = Reporte.objects.all()
        ids_reportes =[]
        for reporte in reportes:
            ids_reportes.append(reporte.id)
        context={
            'reportes': reportes,
            'ids_reportes':ids_reportes,
        }
        return render(request,urlBase+'dashboard.html',context)
    else:
        return redirect(to="login")
    
def newReport(request):
    if request.method !="POST":
        metodos.agregarReporte('reporte',1)
        return redirect(to="home")
    else:
        if request.FILES.get("reporteRt"):
            razon = request.POST["razonRt"]
            reporte = request.FILES.get("reporteRt")
            id_area = request.POST["id_areaRt"]
            fecha_json = request.POST["fecha_DatosRt"]
            objArea = Area.objects.get(id_area=id_area)
            objReporte = Reporte.objects.create(razon=razon,
                                                reporte=reporte,
                                                id_area=objArea,
                                                fecha_json=fecha_json)
            objReporte.save()
            return redirect(to="home")

def excel_to_list(request,file_id):
    reporte = Reporte.objects.get(id=file_id)
    datos = metodos.excel_a_lista(reporte.reporte.path)
    return JsonResponse(datos,safe=False)