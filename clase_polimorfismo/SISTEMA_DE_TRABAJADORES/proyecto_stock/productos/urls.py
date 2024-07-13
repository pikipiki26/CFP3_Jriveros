
from django.urls import path
from .views import *

urlpatterns = [
    path('',Listar_Producto, name='listado_productos'),
    path('crear/',crear_producto, name='crear_producto'),
    path('editar/<id>', Editar_producto, name='Editar_producto'),
    path('actualizar/ <id>', Actualizar_producto, name= 'Actualizar_producto'),
]