from django.shortcuts import render

# Create your views here.
def index(request):
    context ={}
    return render(request,'index.html',context)

def reporte(request):
    context ={}
    return render(request,'reporte.html',context)

def dashboard(request):
    context ={}
    return render(request,'dashboard.html',context)

def login(request):
    context ={}
    return render(request,'login.html',context)