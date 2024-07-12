
from django.urls import path
from .views import *

urlpatterns = [
    path('',Listar_Producto, name='listado_productos'),
]