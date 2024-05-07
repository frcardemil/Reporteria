from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def vistareportes(request):
    return render(request, 'vistareportes.html')