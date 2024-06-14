# class Alumno:
#     def __init__(self,nombre,edad) -> None:
#         self.__nombre= nombre # privado
#         self.edad= edad
#     def get_nombre(self):
#         return self.__nombre
#     def set_nombre(self,nombre2):
#         self.__nombre= nombre2


#esto es una intanciacion ===>>para poder usar la clase 
# alumno1= Alumno("jesi",25)    
# print(alumno1.edad)

#  GET son métodos que se utilizan para acceder al valor de un atributo privado desde fuera de la clase  
# print(alumno1.get_nombre())
 
# #SET son métodos que se utilizan para modificar el valor de un atributo privado desde fuera de la clase
# alumno1.set_nombre("milag")
# print(alumno1.get_nombre())




# Consigna 1: Clase Producto
# Crea una clase Producto que represente un producto en una tienda en línea. La clase debe tener los siguientes atributos privados:

# __nombre: El nombre del producto (cadena de texto).
# __precio: El precio del producto (número decimal).
# __stock: La cantidad de productos disponibles en inventario (número entero).
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre.
# Métodos getter y setter para precio, con una validación en el setter para asegurar que el precio sea positivo.
# Métodos getter y setter para stock, con una validación en el setter para asegurar que el stock sea un número entero no negativo.
# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Producto, se muestre la siguiente información:
# Producto: <nombre>, Precio: <precio>, Stock: <stock>
# class Producto():
#     def __init__(self,nombre,precio,stock) -> None:
#         self.__nombre= nombre
#         self.__precio= precio
#         self.__stock= stock
#     def get_nombre(self):
#         return self.__nombre
#     def set_nombre(self, nombre):
#         self.nombre = nombre
#     def get_precio(self):
#         return self.__precio
#     def set_precio(self,precio):
#         if precio > 0:
#             self.precio= precio
#         else:
#             print("el valor no puede ser negativo")
#     def get_stock(self):
#         return self.__stock
#     def set_stock(self,stock):
#         if stock > 0:
#             self.stock= stock
#         else:
#             print("el stock no puede ser un negativo")
#     def __str__(self) -> str:
#         return f"Producto: {self.__nombre},precio: {self.__precio},stock: {self.__stock}"
    
# #esto es una intanciacion ===>>para poder usar la clase 
# Producto1= Producto("mamon",400,5)
# #GET son métodos que se utilizan para acceder al valor de un atributo privado desde fuera de la clase  
# print(Producto1)
# # print(Producto1.get_precio())
# # print(Producto1.get_stock())

# # #SET son métodos que se utilizan para modificar el valor de un atributo privado desde fuera de la clase
# Producto1.set_precio(-5)
# print(Producto1)
    


# Consigna 2: Clase Empleado
# Crea una clase Empleado que represente a un empleado en una empresa. La clase debe tener los siguientes atributos privados:

# __nombre: El nombre del empleado (cadena de texto).
# __salario: El salario del empleado (número decimal).
# __departamento: El departamento al que pertenece el empleado (cadena de texto).
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre.
# Métodos getter y setter para salario, con una validación en el setter para asegurar que el salario sea positivo.
# Métodos getter y setter para departamento.
# Además, implementa un método aumentar_salario(porcentaje) que incremente el salario del empleado por un cierto porcentaje. Asegúrate de validar que el porcentaje sea un número positivo.

# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Empleado, se muestre la siguiente información:
# Empleado: <nombre>, Salario: <salario>, Departamento: <departamento>
# class Empleado():
#     def __init__(self,nombre,salario,departamento) -> None:
#         self.__nombre= nombre
#         self.__salario=salario
#         self.__departamento= departamento
#     def get_nombre(self):
#         return self.__nombre
#     def set_nombre(self, nombre):
#         self.nombre = nombre
#     def get_salario(self):
#         return self.__salario
#     def set_salario(self,salario):
#         self.salario= salario
#         if salario > 0:           #==> validacion en el setter para asegurar que el salario sea positivo.
#             self.salario=salario
#         else:
#             print("el salario sea positivo")
#     def aumentar(self,aumentar):
#         if aumentar > 0:
#             self.__salario+= self.__salario*(aumentar/100)#incrementamos el salario del empleado por un cierto porcentaje.
#         else:
#             print("EL PORCENTAJE ES POSITIVO")       

#     def get_departamento(self):
#         return self.__departamento
#     def set_departamento(self,departamento):
#         self.departamento= departamento
#     def __str__(self) -> str:
#         return f"Empleado: {self.__nombre},salario: {self.__salario},departamento: {self.__departamento}"

# ##  instanciamos la clase del empleado     
# gobernador= Empleado("guille",850.000,"Nuñes")   
# print(gobernador) 

# gobernador.aumentar(20)
# print(gobernador)
                            

#TODO: Consigna 3: Clase Curso
# Crea una clase Curso que represente un curso en una plataforma educativa. La clase debe tener los siguientes atributos privados:

# __nombre_curso: El nombre del curso (cadena de texto).
# __instructor: El nombre del instructor del curso (cadena de texto).
# __estudiantes: Una lista que contenga los nombres de los estudiantes inscritos en el curso.
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre_curso.
# Métodos getter y setter para instructor.
# Un método getter para obtener la lista de estudiantes get_estudiantes().
# Un método agregar_estudiante(estudiante) que añada un estudiante a la lista de estudiantes.
# Un método remover_estudiante(estudiante) que elimine un estudiante de la lista de estudiantes si existe en la lista.
# Un método listar_estudiantes() que devuelva una cadena con todos los nombres de los estudiantes inscritos, separados por comas.
# Un método __str__ para representar el objeto como una cadena que muestre el nombre del curso y el nombre del instructor.
class Curso:
    def __init__(self,nombre_curso,instructor):
        self.__nombre_curso= nombre_curso
        self.__intructor= instructor
        self.__estudiante= []

    def get_nombre_curso(self):
        return self.__nombre_curso
    def set_nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    def get_instructor(self):
        return self.__instructor
    def set_instructor(self,instructor):
        self.__intructor = instructor

    def get_estudiantes(self):
        return self.__estudiante 
    
    def agregar_estudiante(self,estudiante):
        self.__estudiante.append(estudiante)
      
        
    def remover_estudiante(self,estudiante):
        if estudiante in self.__estudiante:
            self.__estudiante.remove(estudiante)
        else:
            print("el estudiante no esta en la lista")    
    def listar_estudiante(self):
        return ",".join(self.__estudiante)
    
    def __str__(self) -> str:
        return f"curso: {self.__nombre_curso},intructor: {self.__intructor}"


Curso1= Curso("programacion","richar")
Curso1.agregar_estudiante("jose")
Curso1.agregar_estudiante("maxi")
Curso1.listar_estudiante()
# print(Curso1.get_estudiantes())
# print(Curso1.agregar_estudiante())        


# estudiantes = []
# estudiantes.append(2)
# print(estudiantes)



