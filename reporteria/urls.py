from django.urls import path,include
from reporteria.api.router import router_reporte
from . import views

urlpatterns = [
    path('api/',include(router_reporte.urls)),
    path('login/', views.valLogin,name='login'),
    path('logOut/', views.logOutReport,name='logOutR'),
    path('', views.reporte,name='home'),
    path('newReport/', views.newReport,name='newReporte'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('excelList/<int:file_id>/', views.excel_to_list, name='excelList'),
    path('eliminarRt/<str:pk>/', views.eliminarRt, name='eliminarRt'),
    path('modificarRt/', views.modificarRt, name='modificarRt'),
]