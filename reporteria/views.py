from os import stat
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReporteDespacho 
from .serializer import ReporteDespachoSerializer
import requests

from copy import deepcopy
    
urlBase="reporteria/contenido/"

class ReporteDespachoViewSet(viewsets.ModelViewSet):
    queryset = ReporteDespacho.objects.all()
    serializer_class = ReporteDespachoSerializer

    def create(self, request, *args, **kwargs):
        url = 'http://44.205.221.190:8000/despachos/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            despachos = data.get('results', [])

            total_despachos = len(despachos)
            entregados = sum(1 for despacho in despachos if despacho['entregado'] == True)
            no_entregados = total_despachos - entregados

            reporte_despacho = ReporteDespacho.objects.create(
                cantidad_de_despachos=total_despachos,
                entregados=entregados,
                no_entregados=no_entregados
            )
            reporte_despacho.save()

            serializer = self.get_serializer(reporte_despacho)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        else:
            print("Error al obtener los datos de la API")
            return Response({'error': 'Error al obtener los datos de la API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




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