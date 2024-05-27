from os import stat
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import ReporteSerializer
from .models import Reporte
import requests
from copy import deepcopy
from django.http import QueryDict
from datetime import datetime
    
urlBase="reporteria/contenido/"

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

    def create(self, request, *args, **kwargs):
        despacho_url = 'http://44.205.221.190:8000/despachos/'
        response = requests.get(despacho_url)
        body= request.data.copy()
        if response.status_code == 200:
            data = response.json()
            fecha_despacho = None
            for despacho in data['results']:
                fecha_despacho = despacho.get('fecha_despacho')
                if fecha_despacho:
                    break
            
            if fecha_despacho:
                body['fecha_despacho'] = datetime.strptime(fecha_despacho, '%Y-%m-%d').date()
                    
        querydict=QueryDict('data',mutable=True)
        querydict.data=body
        print(querydict.data)
        return super().create(querydict, *args, **kwargs)



def valLogin(request):
    if not request.user.is_authenticated:
        if request.method != "POST":
            return render(request,urlBase+'login.html')
        else:
            usuario = request.POST["ususarioLog"]
            contrasena = request.POST["contrasenaLog"]
            try:
                remember = request.POST["remember"]
                remember = True
            except:
                remember = False
            user=authenticate(username=usuario,password=contrasena)
            if (user):
                print('Usuario de reporteria encontrado ',user)
                print(remember)
                login(request,user)
                return redirect(to='home')
            else:
                print('Usuario no pertenece a reporteria')
                return render(request,urlBase+'login.html')
    else:
        return redirect(to='home')
    
def logOutReport(request):
    logout(request)
    return redirect(to='home')

def index(request):
    if request.user.is_authenticated:
        return render(request,urlBase+'index.html')
    else:
        return redirect(to="login")
    
def reporte(request):
    if request.user.is_authenticated:
        return render(request,urlBase+'reporte.html')
    else:
        return redirect(to="login")
    
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,urlBase+'dashboard.html')
    else:
        return redirect(to="login")