from django.shortcuts import render
from .models import Producto
# Create your views here.
def Listar_Producto(request):#es una petision
    productos=Producto.objects.all()
    return render(request,"productos.html",{'productos':productos})