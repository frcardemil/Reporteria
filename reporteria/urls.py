from django.urls import path,include
from reporteria.api.router import router_reporte
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', views.valLogin,name='login'),
    path('logOut/', views.logOutReport,name='logOutR'),
    path('', views.reporte,name='home'),
    path('newReport/', views.newReport,name='newReporte'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('eliminarRt/<str:pk>/', views.eliminarRt, name='eliminarRt'),
    path('modificarRt/<str:pk>/', views.modificarRt, name='modificarRt'),
    path('newExcel/<str:open>/<str:pk>/', views.newExcel, name='newExcel'),
    path('api/',include(router_reporte.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]