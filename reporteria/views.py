from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from .models import ReporteGeneral
from . import metodos
from django.utils import timezone

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
        reportes=[]
        for reporteTMP in ReporteGeneral.objects.all().order_by('-anno_mes_rt'):
            reporte={
                'id':reporteTMP.anno_mes_rt,
                'anno_mes_rt':str(reporteTMP),
                'porc_entrega_tiempo':round((reporteTMP.entrega_a_tiempo/reporteTMP.entrega_total)*100,2),
                'porc_new_stock':round((reporteTMP.adquisicion_recibida/reporteTMP.stock_productos)*100,2),
                'porc_venta_defin':round((reporteTMP.venta_realizada/reporteTMP.venta_pedido)*100,2),
                'porc_factu_pagada':round((reporteTMP.factura_pagada/reporteTMP.factura_total)*100,2),
            }
            reportes.append(reporte)
        context={
            'reportes':reportes,
        }
        return render(request,urlBase+'reporte.html',context)
    else:
        return redirect(to="login")

def eliminarRt(request,pk):
    if request.user.is_superuser:
        objReporte=ReporteGeneral.objects.get(anno_mes_rt=pk)
        objReporte.delete()
        return redirect('home')
    else:
        return redirect('login')
    
def modificarRt(request):
    if request.method !="POST":
        return redirect(to="home")
    else:
        return redirect(to="home")

def dashboard(request):
    if request.user.is_authenticated:
        fechaActual=timezone.now().date()
        finalAño=fechaActual.year*100+12
        try:
            reportes = ReporteGeneral.objects.filter(anno_mes_rt__range=(finalAño-11, finalAño)).order_by('-anno_mes_rt')
            print("hola mundo xd")
            context={
                'reportes': reportes,
            }
            return render(request,urlBase+'dashboard.html',context)
        except ReporteGeneral.DoesNotExist:
            print("No se encontró ningún ReporteGeneral para el mes y año especificados.")
            return render(request,urlBase+'dashboard.html')
    else:
        return redirect(to="login")

def newReport(request):
    if request.method =="POST":
        anno_mes_rt_Post = request.POST["newRt"]
        objReporte = ReporteGeneral.objects.create(anno_mes_rt=anno_mes_rt_Post,
                                                   entrega_total=1,
                                                   entrega_a_tiempo=1,
                                                   stock_productos=1,
                                                   pedido_proveedor=1,
                                                   adquisicion_recibida=1,
                                                   venta_pedido=1,
                                                   venta_realizada=1,
                                                   factura_total=1,
                                                   factura_pagada=1)
        objReporte.save()
        return redirect(to="home")
    else:
        return redirect(to="home")
    
def newExcel(request,open,pk):
    id= int(pk)
    try:
        reporte = ReporteGeneral.objects.get(anno_mes_rt=id)
        print(open)
        if open=='1':
            metodos.agregarReporte("RT-"+pk,True,reporte)
        elif open=='2':
            metodos.agregarReporte("RT-"+pk,False,reporte)
        else:
            print('else')
        return redirect(to="home")
    except:
        print('no existe el reporte')
        return redirect(to="home")