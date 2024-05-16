from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.valLogin,name='login'),
    path('reporte/', views.reporte,name='reporte'),
    path('dashboard/', views.dashboard,name='dashboard'),
]