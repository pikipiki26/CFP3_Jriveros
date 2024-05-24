

#importamos el mudulo principal
# LIBRERIA TKINTER ==>ENTORNO GRAFICO
from tkinter import * 
from tkinter import messagebox
from logica_de_contraseña import validar_usuario

#funcion que se llama al hacer click en el boton "iniciar sesion"
def iniciar_sesion():
    usuario = nombreEntry.get()#obtener el texto en el campo usuario
    contraseña = contraseñaEntry.get()
   
    if validar_usuario(usuario,contraseña):
      messagebox.showinfo("exito","inisio de sesion exitoso")
    else:
        messagebox.showerror("error","usuario o contraseña invalido")    

#ventana principal
root=Tk()#HAGO instanciacion con la palabra (root)
root.title("login de usuario")#asigna un titulo a la  ventana
#primcipal
root.geometry("300x250")#le asigno las medidas de mis ventana
root.config(bg="blue")#aca le asigno un color de fondo

#instanciamos tambien la palabra (maiframe)
maiframe= Frame(root)#
maiframe.grid(row=0,column=0 ,padx=20,pady=20)# le instancio en donde quiro posicionarlo
maiframe.config(width=250,height=230)#instanciamos un espaciado alto y bajo

#instanciamos tambien la palabra (label)
titulo= Label(maiframe,text="login de usuario",font=("arial",24))#
titulo.grid(column=0,row=0,columnspan=2,pady=10)#instancio donde quiero posicionsrlo


#elementos label y entry  usuario 
nombrelabel=Label(maiframe, text=("usuario: "))
nombrelabel.grid(column=0,row=1,sticky=W,pady=5)


#input usuario
nombreEntry=Entry(maiframe,width=30)
nombreEntry.grid(column=1,row=1,pady=5)


#elementos label y entry de contraseña
contraseñalabel= Label(maiframe,text=("contraseña:"))
contraseñalabel.grid(column=0,row=2,sticky=W,pady=5)

#input contraseña
contraseñaEntry=Entry(maiframe,width=30,show="*")
contraseñaEntry.grid(column=1,row=2,pady=5)


#BOTON
IniciarSesionBTN= Button(maiframe,text=("iniciar sesion"),command=iniciar_sesion)
IniciarSesionBTN.grid(column=0,row=3,columnspan=2,pady=20)



root.mainloop()



