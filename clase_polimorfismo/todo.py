class Empleado:
    def init(self,nombre,id_empleado) -> None:
        self.__nombre=nombre # privada
        self.__id_empleado=id_empleado #privada

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre2):
        self.__nombre= nombre2

    def get_id_empleado(self):
        return self.get_id_empleado
    def set_id_empleado(self,id_2):
        self.set_id_empleado=id_2

    def calcular_salario(self):
        return self.calcular_salario        

    def descripcion (self) -> str:
        return F"Empleado: {self._nombre},id_empleado: {self._id_empleado} "

#2- Subclases:
class EmpleadoTiempoCompleto(Empleado):
    def init(self, nombre, id_empleado,salario_mensual) -> None:
        super().init(nombre, id_empleado)
        self.__salario_mensual= salario_mensual #privada
      
    def get_salario_mensual(self):
        return self.__salario_mensual
    def set_salario_mensual(self,salario):
        self.__salario_mensual= salario

    def calcular_salario(self):
        return self.__salario_mensual

    def str(self) -> str:
        #sobreescribe el metodo de empleado
        return f"{super()._str()},salario_mensual: {self._salario_mensual} " 

class EmpleadoMedioTiempo(Empleado):
    def init(self, nombre, id_empleado,salario_por_hora,horas_trabajadas) -> None:
        super().init(nombre, id_empleado) 
        self.__salario_por_hora= salario_por_hora #privado
        self.__horas_tabajadas= horas_trabajadas #privado

    def get_salario_por_hora(self):
        return self.__salario_por_hora
    def set_salario_por_hora(self,salario):
        self.__salario_por_hora= salario

    def get_horas_trabajadas(self):
        return self.__horas_tabajadas
    def set_hora_trabajadas(self,trabajo):
        self.__horas_tabajadas= trabajo

    def calcular_salario(self):
        return self._salario_por_hora *self._horas_tabajadas     

    def str(self) -> str:
        return f"salario_por_hora: {self._salario_por_hora}, hora_trabajadas: {self._horas_tabajadas}" 

class EmpleadoFreelance(Empleado):
    def init(self, nombre, id_empleado,tarifa_proyecto) -> None:
        super().init(nombre, id_empleado)
        self.__tarifa_proyecto=tarifa_proyecto #privada

    def get_tarifa_proyecto(self):
        return self.__tarifa_proyecto
    def set_tarifa_proyecto(self,tarifa):
        self.__tarifa_proyecto= tarifa


    def calcular_salario(self):
        return self.__tarifa_proyecto 


    def str(self) -> str:
        return f"{super()._str()},tarifa_proyecto: {self._tarifa_proyecto}"
    
#3- Gestion de Empleados
    # - class GestionEmpleados
        # - Atributo: lista_empleados
    # - Metodos:
        # - agregar_empleado()
        # - agregar_varios_empleados()
        # - eliminar_empleado_por_id()
        # - mostrar_empleados()
        #- calcular_salarios() : Calcular y devolver la suma de todos los salarios de todos los empleados de la lista
        # - str : Una representación en cadena de la lista de nombres de empleados
class GestionEmpleados:
    def init(self) -> None:
        self.lista_empleados= []

    def agregar_empleado(self,empleado):
        self.lista_empleados.append(empleado) 

    def agregar_varios_empleados(self,*empleados):#*args metodos para agregar varios atributos
        for empleado in empleados:
            self.agregar_empleado(empleado)

    def Eliminar_empleado_por_id(self,id_empleado):
        if any(emp.get_id_embleado()== id_empleado for emp in self.lista_empleados):
         self.lista_empleados=[emp for emp in self.lista_empleados if emp.get_id_empleado() != id_empleado]
         print(f"empleado con ID {id_empleado} eliminado exitosamente")
        else:
            print(f"empleado con ID {id_empleado} no encontrado.")

    def mostrar_empleados(self):
        for emp in self.lista_empleados:
            print (emp)

    def calcular_salario_totales(self):
        return sum(emp.calcular_salario() for emp in self.lista_empleados)
    def _str_(self) -> str:
        nombres=[emp.get_nombre()for emp in self.lista_empleados]
        return f"empleados: "+",".join(nombres)
    
def mostrar_menu():
    print("\n gestion de empleado")
    print("1. agregar empleado")
    print("2. agregar varios empleados")
    print("3. eliminar empleado por ID")
    print("4. mostrar empleado")
    print("5. salarios totales ")
    print("6. salir")




def main():
 gestion= GestionEmpleados()
 while True:
    mostrar_menu()
    opcion= input("ingrese una opcion: ")
    if opcion == "1":
        print("empleado agregada: ")
        tipo=input("ingreses el tipo de empleado: (tirmpo completo,medio tiempo,freelance").lower()
        empleado=seleccionar_empleado(tipo)
        gestion= agregar_empleado(empleado)
        print("empleado agregada exitosamente.")
    elif opcion =="2":
        print("\nagregando  varios empleandos.")
        num_empleado=int(input("ingrese el numero de empleados a agregar."))
        empleados=[]
        for i in range(num_empleado):
            tipo= input(ingrese el tipo de empleado: (t))

        
    elif opcion=="3":
        print("eliminando id empleado") 
    elif opcion=="4":
        print("mostrar empleado")       
        break
    else:
        print(" opcion no valida, intentelo  nuevamente")
       
def seleccionar_empleado(self):
    tipos_empleados= int(input("""
                            "seleccione el tipo de empleados"
                            1. EmpleadoTiempoCompleto 
                            2. EmpleadoMedioTiempo
                            3. Empleadofreelance           
                                """
                               ))
    Nombre=input("ingrese el nombre del empleado")
    Id=input("ingrese el ai del empleado")     
    if tipos_empleados=="salario completo":
        salario_mensual=input("ingrese el salario mensual: ")
        return EmpleadoTiempoCompleto(Nombre,Id,salario_mensual)
    elif tipos_empleados==" medio completo":
        salario_por_hora=float(input("ingrese el salario por hora: ")
        horas_trabajadas=int(input("ingrese las horas tranajadas: ")
        return EmpleadoMedioTiempo(Nombre,Id,salario_por_hora,horas_trabajadas)
    elif tipos_empleados=="freelance":
        tarifa_proyecto=float(input("ingrese la tarifa del proyecto: ")
        return EmpleadoFreelance(Nombre,Id,tarifa_proyecto)
    else:
        print("datos incorrecta")

main()