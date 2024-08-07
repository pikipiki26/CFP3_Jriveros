from django.shortcuts import render,redirect
from .models import Producto
# Create your views here.
def Listar_Producto(request):#es una petision
    productos=Producto.objects.all()
    return render(request,"productos.html",{'productos':productos})

def crear_producto(request):
    nombre =request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    precio = request.POST["precio"]
    stock = request.POST["stock"]   
    producto= Producto(nombre= nombre, descripcion=descripcion,precio=precio,stock=stock)
    producto.save()
    return redirect('/inventario')


def Editar_producto(request,id):
    producto= Producto.objects.get(id=id)
    return render(request, 'Editar_producto.html',{'producto': producto})

def Actualizar_producto(request,id):
    producto=Producto.objects.get(id=id)
    nombre =request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    precio = request.POST["precio"]
    stock = request.POST["stock"]   
    producto.nombre= nombre
    producto.descripcion= descripcion
    producto.precio= precio
    producto.stock= stock
    producto.save()
    return redirect('/inventario')
