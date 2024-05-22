
#TODO:Creacion de clase Personaje
class Personaje:
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print("Nombre: ", self.nombre)
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: " , self.defensa)
        print("Vida: ", self.vida)
        
    def subir_nivel(self,fuerza, inteligencia, defensa,vida):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.vida = self.vida + vida
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} esta muerto")
        
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
        #return f"El daño causado por {self.nombre} es de {self.fuerza - enemigo.defensa} al rival {enemigo.nombre}"
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} ha realizado {daño} puntos al rival {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es de {enemigo.vida}")
        else:
            enemigo.morir()
        


# return self.fuerza + self.espada - enemigo.defensa


# roberto = Guerrero("Roberto",100,80,60,600,2)
# roberto.atributos()
# roberto.cambiar_arma()
# jesica = Personaje("Jesica", 100, 89, 100,800)
# roberto.atacar(jesica)
# print("\n")
# jesica.atributos()
# roberto = Guerrero("Roberto",100,80,60,600,2)
# roberto.atributos()
# roberto.cambiar_arma()
# jesica = Personaje("Jesica", 100, 89, 100,800)
# roberto.atacar(jesica)
#jesica.atacar(roberto)
# print("\n")
# jesica.atributos()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo

    def cambiar_hechizo(self):
        tipo_hechizo = int(input("""
                Seleccione el tipo de arma:
                1- Magia Negra - daño 25
                2- Baston Magico - daño 70
                3- Vara Encantada - daño 80
                4- Libro Oscuro - daño 100
                """
                ))
        if tipo_hechizo == 1:
            self.hechizo = 25
        elif tipo_hechizo == 2:
            self.hechizo = 70
        elif tipo_hechizo == 3:
            self.hechizo = 80
        elif tipo_hechizo == 4:
            self.hechizo = 100
        else:
            print("Elección incorrecta")

    #Sobreescribir el metodo atributos()
    def atributos(self):
        super().atributos()
        print(f"Hechizo: {self.hechizo}")

    #Sobreescribir el metodo daño()
    def daño(self,enemigo):
        return self.inteligencia + self.hechizo - enemigo.defensa
    

class Guerrero(Personaje):
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.espada = espada
        
    # Metodo que nos permite seleccionar un arma
    def cambiar_arma(self):
        tipo_arma = int(input("""
                              Seleccione el tipo de arma:
                              1- Doran - daño 12
                              2- Filo Infinito - daño 70
                              3- Sanguinaria - daño 80
                              4- Espadon - daño 100
                              """
                              ))
        #Logica al elegir el arma.
        if tipo_arma == 1:
            self.espada = 12
        elif tipo_arma == 2:
            self.espada = 70
        elif tipo_arma == 3:
            self.espada = 80
        elif tipo_arma == 4:
            self.espada = 100
        else:
            print("Opción no valida")
        
    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")
        
    #Sobreescribir el metodo daño, ya que incorporamos una accesorio al guerrero
    def daño(self,enemigo):
        return self.fuerza + self.espada - enemigo.defensa

#simular pelea
tomas= Mago("toomas",90,120,160,400,40)
milagros= Guerrero("milagros",95,120,150,450,40)
#nombre ,fuerza ,inteligencia,defenza
def combate(jugador_1,jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n turno: {turno}")
        print(f"anccion de (jugador_1.nombre)")
        jugador_1.atacar(jugador_2)
        print(f"accion dee (jugador_2.nombre")
        jugador_2.atacar(jugador_1)
        turno += 1

#depues de salir del bucle ,imprimo el ganador
    if jugador_1.esta_vivo():
        print(f"\n {jugador_1.nombre} ha ganado")
    elif jugador_2.esta_vivo():
        print(f"\n{jugador_2.nombre} ha ganado")
    else:
        print("\n la pelea fue todo un exito,que termino en ambate")

combate(tomas,milagros)                   

