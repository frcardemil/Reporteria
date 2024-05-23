from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.valLogin,name='login'),
    path('logOut/', views.logOutReport,name='logOutR'),
    path('reporte/', views.reporte,name='reporte'),
    path('newReport/', views.newReport,name='newReporte'),
    path('dashboard/', views.dashboard,name='dashboard'),
]