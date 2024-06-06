from django.urls import path,include 
from rest_framework import routers
from . import views

router=routers.DefaultRouter()


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index,name='home'),
    path('login/', views.valLogin,name='login'),
    path('logOut/', views.logOutReport,name='logOutR'),
    path('reporte/', views.reporte,name='reporte'),
    path('dashboard/', views.dashboard,name='dashboard'),
]