#TODO: crear una clase llamada "libro"que represente un libro. la clase debe tener los sigientes  atributros: titulo,autor,paginas,editorial,fecha-Publicacion. Y un metodo  lamado "informacion"que imprima todos los datos del libro. Crear 2 objetos de la clase libro

class libro():
    pass

#FORMA 1
class libro():
    def __init__(self,titulo,autor,paginas,auditorial,fecha_publicacion):
        self.titulo = titulo
        self.autor =autor
        self.paginas = paginas
        self.auditorial = auditorial
        self.fecha_publicacion = fecha_publicacion

    def informacion(self):
        print(f"el titulo del libro es  {self.titulo}")
        print(f"y el autor del libro es{self.autor}")
        print(f"tiene {self.paginas} paginas")
        print(f"el editorial es {self.auditorial}")
        print(f"la fecha de la publicacion es {self.fecha_publicacion}")

libro1 = libro("el alquimista","paulo cohello",456,"genios",1999)
libro2= libro("condorito","jessi",215,"condor",12554)

libro1.informacion()
libro2.informacion()



#FORMA 2
class libro():
    def __init__(self,titulo,autor,paginas,auditorial,fecha_publicacion):
        self.titulo = titulo
        self.autor =autor
        self.paginas = paginas
        self.auditorial = auditorial
        self.fecha_publicacion = fecha_publicacion

    def informacion(self):
        info_str= (
        f"el titulo del libro es  {self.titulo}\n"
        f"y el autor del libro es{self.autor}\n"
        f"tiene {self.paginas} paginas\n"
        f"el editorial es {self.auditorial}\n"
        f"la fecha de la publicacion es {self.fecha_publicacion}\n"

        )

        with open("informacio.txt","a") as archivo: 
             #==> with ==> metodo que me permite trabajar con recurso que se necesitan ser cerrados despues de uso.
            archivo.write(info_str)
            archivo.write("\n")

    print("innformacion guardada con exito.") 

libro1 = libro("el alquimista","paulo cohello",456,"genios",1999)
libro2= libro("condorito","jessi",215,"condor",12554)

libro1.informacion()
libro2.informacion()