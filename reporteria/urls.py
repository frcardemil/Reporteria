from django.urls import path
from . import views

urlpatterns = [
    path('', views.valLogin,name='login'),
    path('home', views.index,name='home'),
]