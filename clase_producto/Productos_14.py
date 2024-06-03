

#instalamos los modulos 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from Dt_BD_Producto import obtener_productos



def validar_datos():
    return len(productoEntry.get())!=0 and len(cantidadEntry.get())!=0


#metodos de agregar productos
def agregar_producto():
    from  Dt_BD_Producto import insertar_Productos
    if validar_datos():
        producto = productoEntry.get()
        sector = sectorEntry.get()
        cantidad = cantidadEntry.get()
        stock = stockEntry.get()
        insertar_Productos(producto,sector,cantidad,stock)
#limpiamos los campos de entradas (inicio:fin)
        productoEntry.delete(0,END)
        sectorEntry.delete(0,END)
        cantidadEntry.delete(0,END)
        stockEntry.delete(0,END)
    else:
        print("todos los campos son requeridos")
    obtener_producto()


def obtener_producto():
    from Dt_BD_Producto import obtener_productos
    #obtener todas las filas actualizadas de mi tabla
    grabados= grilla.get_children()
    for elementos in grabados:
        grilla.tree.delete(elementos)
        #consulto los datos #==> llamar la funcion obtener_productos para obtener los productos de la DB(BASE DATOS)
    productos=obtener_productos()
    for row in productos:
        grilla.insert('',0,text=row[1],values=row[3])    



ventana= Tk()#HAGO instanciacion con la palabra (ventana)
ventana.title("PRODUCTOS")#asigna un titulo a la  ventana principal
ventana.geometry("500x500")#le asigno las medidas de mi ventana
ventana.config(bg="white")

# maiframe= Frame(ventana)# le pasamos la ventana prncipal
# maiframe.grid(row=0,column=0 ,padx=50,pady=50)# le instancio en donde quiro posicionarlo en columnas y fials
# maiframe.config(width=500,height=500)#instanciamos un espaciado de ancho y lago

#HINTANCIO LA PALABRA (LABEL)
frame= LabelFrame(ventana,text="PRODUCTOS REGISTRADOS",font=("arial",24))
frame.grid(column=0,row=0,columnspan=2,pady=1)#instancio donde quiero posicionsrlo


#elementos label y entry  usuario
productolabel=Label(frame, text=("PRODUCTO: "))
productolabel.grid(column=0,row=1,sticky=W,pady=5)
#input producto
productoEntry=Entry(frame,width=30)
productoEntry.grid(column=1,row=1,pady=5)

#elementos label y entry  usuario
sectorlabel=Label(frame, text=("PROOVEDOR: "))
sectorlabel.grid(column=0,row=2,sticky=W,pady=5)
#input sector
sectorEntry=Entry(frame,width=30)
sectorEntry.grid(column=1,row=2,pady=5)

#elementos label y entry  usuario
cantidadlabel=Label(frame, text=("CANTIDAD: "))
cantidadlabel.grid(column=0,row=3,sticky=W,pady=5)
#input cantidad
cantidadEntry=Entry(frame,width=30)
cantidadEntry.grid(column=1,row=3,pady=5)

#elementos label y entry  usuario
Descripcionlabel=Label(frame, text=("DESCRIPCION: "))
Descripcionlabel.grid(column=0,row=4,sticky=W,pady=5)
#input stock
stockEntry=Entry(frame,width=30)
stockEntry.grid(column=1,row=4,pady=5)


#BOTON
IngresarBTN= Button(frame,text=("INGRESAR"),command=agregar_producto)
IngresarBTN.grid(column=0,row=5,columnspan=2)

AñadirBTN= Button(frame,text=("AÑADIR"))
AñadirBTN.grid(column=1,row=5,columnspan=5)

ModificarBTN= Button(frame,text=("MODIFICAR"))
ModificarBTN.grid(column=2,row=5,columnspan=3)


grilla=ttk.Treeview(height=10,columns=2)#un contenedor donde muestra todo los registros
grilla.grid(column=0,row=6)

grilla.heading("#0",text="PRODUCTO")
grilla.heading("#1",text="CANTIDAD")

obtener_productos()
ventana.mainloop()