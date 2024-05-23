

#importamos el mudulo principal

from tkinter import * 
from tkinter import messagebox
#ventana principal
root=Tk()
root.title("login de usuario")#asigna un titulo a la  ventana
#primcipal
root.geometry("300x250")
root.config(bg="red")

maiframe= Frame(root)
maiframe.grid(row=0,column=0 ,padx=20,pady=20)
maiframe.config(width=250,height=230)


titulo= Label(maiframe,text="login de usuario",font=("arial",24))
titulo.grid(column=0,row=0,columnspan=2,pady=10)


#elementos label de usuario y contraseña
nombrelabel=Label(maiframe, text=("usuario:"))
nombrelabel.grid(column=0,row=1,sticky=W,pady=5)


#input usuario
nombreEntry=Entry(maiframe,width=30)
nombreEntry.grid(column=1,row=1,pady=5)
#elementos label y entry de contraseña
contraseñalabel= Label(maiframe,text=("contraseña:"))
contraseñalabel.grid(column=0,row=2,sticky=W,pady=5)

contraseñaEntry=Entry(maiframe,width=30,show="*")
contraseñaEntry.grid(column=1,row=2,pady=5)


#BOTON
IniciarSesionBTN= Button(maiframe,text=("iniciar sesion"))
IniciarSesionBTN.grid(column=0,row=3,columnspan=2,pady=20)



root.mainloop()



