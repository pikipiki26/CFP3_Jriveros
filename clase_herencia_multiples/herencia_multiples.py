# #TODO: herencia mutiples==>

# class calseA:
#     def metodo_a(self):
#         return "metood de calseA"
# class ClaseB:
#     def metodo_b():
#         return "metodo de clsseB"
# class ClaseDerivada(calseA,ClaseB):
#     def metodo_derivada():
#         return "metood claseDerivada" 

# ObjetoDeri=ClaseDerivada()# se hereda todos los metodos (a,b) desde mi ==>(ObjetoDeri)

# #llamara los metodos  de las clases padres 
# print(ObjetoDeri.metodo_a())#==> salidad : metodo clase A
# print(ObjetoDeri.metodo_b())#==>  salidad : metodo clase B
# print(ObjetoDeri.metodo_derivada())#==>  salidad : metodo clase Derivada 

#consigna : mediante el uso de herencia multiples represent ar distintos tipos de vehiculos,para combinar las caracteristicas de tipos de vehiculos

class Vehiculos:
    def __init__(self, marcas, modelos, color,altura,asientos) -> None:
        self.marcas = marcas
        self.modelo = modelos
        self.color = color
        self.altura = altura
        self.asientos = asientos

    def Ensender(self):
        self.ensendido=True
        print("el vehiculo esta ensendido")
        
    def Apagar(self):
        self.ensendido=False
        print("el vehiculo esta apagada")

    def descripcion():
        return"marcas: {self.marcas},color: {self.color},altura: {self.altuta}, asientod: {self.asientos}"      
      
class Auto(Vehiculos):
    def __init__(self, marcas, modelos,color,altura,asientos,motor) -> None:
        super().__init__(marcas, modelos,color,altura,asientos)
        self.motor= motor

    def Conducir(self):
        #metodo especifico de auto para conducir
        print("estouy conduciendo")

    def descripcion(self):
          #sobreescribe el metodo de vehiculo para agregar mas detalles de auto
        return f"{super().descripcion()},motor: {self.motor}"

class Avion (Vehiculos):
    def __init__(self, marcas, modelos, color, altura, asientos,alas,tipo_motor) -> None:
        super().__init__(marcas, modelos, color, altura, asientos)
        self.alas= alas
        self.tipo_motor= tipo_motor  

    def volar(self):
        #metodo especifico del avion para volar
        print("volando el avion")

    def descripcion(self):
        #sobreescribe el metodo de vehiculo para agregar mas detalles de avion
        return f"{super().descripcion()},alas: {self.alas},motor: {self.tipo_motor}" 



class vehiculoAmfibio(Auto,Avion):
    def __init__(self, marcas, modelos, color, altura, asientos,motor,alas,tipo_motor,capacidad_agua) -> None:
        self.marcas = marcas
        self.modelo = modelos
        self.color = color
        self.altura = altura
        self.asientos = asientos
        self.motor= motor
        self.alas= alas
        self.tipo_motor= tipo_motor 
        self.capacidad_agua= capacidad_agua
        
    def navegar(self):
        print("navegando el vehiculo amfibio")

    def descripcion(self):
        #sobreescribe el metodo de vehiculo para agregar mas detalles de vehiculoamfibio
        return f"{super().descripcion()},capacidad_agua: {self.capacidad_agua}"
    

vehiculo_amfibio= vehiculoAmfibio("amphico","honda x","azul","2metros",4,"turbojet",2,"hibrido",500) 
print(vehiculo_amfibio.descripcion())   




        