from django.shortcuts import render,redirect
from . import metodos,metApis
from .models import ReporteGeneral
from django.utils import timezone
from localStoragePy import localStoragePy

# Create your views here.

urlBase="reporteria/contenido/"
localStorage = localStoragePy('reporteria', 'json')

def valLogin(request):
    if not localStorage.getItem('user'):
        if request.method != "POST":
            return render(request,urlBase+'login.html')
        else:
            usuario = request.POST["ususarioLog"]
            contrasena = request.POST["contrasenaLog"]
            user = {
                'username':usuario,
                'password':contrasena,
            }
            if (metApis.seguridadApi(usuario,contrasena)):
                print('Usuario de reporteria encontrado ('+usuario+')')
                localStorage.setItem('user',user)
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
    localStorage.removeItem('user')
    return redirect(to='home')

def calcularPorc(a,b):
    try:
        porc= round((a/b)*100,2)
    except:
        porc = '--'
    return porc

def reporte(request):
    if localStorage.getItem('user'):
        reportes=[]
        for reporteTMP in ReporteGeneral.objects.all().order_by('-anno_mes_rt'):
            reporte={
                'id':reporteTMP.anno_mes_rt,
                'anno_mes_rt':str(reporteTMP),
                'porc_entrega_tiempo':calcularPorc(reporteTMP.entrega_a_tiempo,reporteTMP.entrega_total),
                'porc_new_stock':calcularPorc(reporteTMP.pedido_proveedor,reporteTMP.stock_productos),
                'porc_venta_defin':calcularPorc(reporteTMP.boleta_pagada,reporteTMP.boleta_total),
                'porc_factu_pagada':calcularPorc(reporteTMP.factura_pagada,reporteTMP.factura_total),
            }
            reportes.append(reporte)
        context={
            'reportes':reportes,
        }
        return render(request,urlBase+'reporte.html',context)
    else:
        return redirect(to="login")

def eliminarRt(request,pk):
    if localStorage.getItem('user'):
        objReporte=ReporteGeneral.objects.get(anno_mes_rt=pk)
        objReporte.delete()
        return redirect('home')
    else:
        return redirect('login')
    
def modificarRt(request,pk):
    if localStorage.getItem('user'):
        anno=int(round(int(pk)/100,0))
        mesTmp=int(pk)-anno*100
        if mesTmp < 10:
            mes='0'+str(mesTmp)
        else:
            mes=str(mesTmp)
        objReporte=ReporteGeneral.objects.get(anno_mes_rt=pk)
        reporteApi=metApis.obtenerRG(str(anno),mes)
        objReporte.entrega_total=reporteApi["entrega_total"]
        objReporte.entrega_a_tiempo=reporteApi["entrega_a_tiempo"]
        objReporte.stock_productos=reporteApi["stock_productos"]
        objReporte.pedido_proveedor=reporteApi["pedido_proveedor"]
        objReporte.adquisicion_recibida=reporteApi["adquisicion_recibida"]
        objReporte.venta_pedido=reporteApi["venta_pedido"]
        objReporte.venta_realizada=reporteApi["venta_realizada"]
        objReporte.factura_total=reporteApi["factura_total"]
        objReporte.factura_pagada=reporteApi["factura_pagada"]
        objReporte.boleta_total=reporteApi["boleta_total"]
        objReporte.boleta_pagada=reporteApi["boleta_pagada"]
        objReporte.save()
        return redirect('home')
    else:
        return redirect('login')

def dashboard(request):
    if localStorage.getItem('user'):
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
    if localStorage.getItem('user'):
        if request.method =="POST":
            anno_mes_rt_Post = request.POST["newRt"]
            anno_mes_rt_Tmp = str(anno_mes_rt_Post).split('-')
            anno_mes_rt = int(anno_mes_rt_Tmp[0]+anno_mes_rt_Tmp[1])
            print(anno_mes_rt_Tmp[0])
            print(anno_mes_rt_Tmp[1])
            reporteApi=metApis.obtenerRG(anno_mes_rt_Tmp[0],anno_mes_rt_Tmp[1])
            objReporte = ReporteGeneral.objects.create(anno_mes_rt=anno_mes_rt,
                                                    entrega_total=reporteApi["entrega_total"],
                                                    entrega_a_tiempo=reporteApi["entrega_a_tiempo"],
                                                    stock_productos=reporteApi["stock_productos"],
                                                    pedido_proveedor=reporteApi["pedido_proveedor"],
                                                    adquisicion_recibida=reporteApi["adquisicion_recibida"],
                                                    venta_pedido=reporteApi["venta_pedido"],
                                                    venta_realizada=reporteApi["venta_realizada"],
                                                    factura_total=reporteApi["factura_total"],
                                                    factura_pagada=reporteApi["factura_pagada"],
                                                    boleta_total=reporteApi["boleta_total"],
                                                    boleta_pagada=reporteApi["boleta_pagada"])
            objReporte.save()
            return redirect(to="home")
        else:
            return redirect(to="home")

from pathlib import Path

def newExcel(request,open,pk):
    id= int(pk)
    ruta_del_archivo = Path("/media/excel_files/RT-"+pk+'.xlsx')
    if ruta_del_archivo.exists():
        ruta_del_archivo.unlink()
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
    