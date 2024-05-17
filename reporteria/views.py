from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User

# Create your views here.

urlBase="reporteria/contenido/"

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