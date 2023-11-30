    

# # # todo: #fuenciones

# # # def saludar():
# # #     print("hola mundo")


# # # saludar() 
# # nombre= "jesi"
# # print(f"hola{nombre}") #primer paso

# # #2do paso 
# # def saludar_nombre(nomre):# se le llama parametros
# #     print(f"hola {nomre}")
# # saludar_nombre("ronald") # y cuando la invoco se llama argumento   


# def prueba ():
#     numero=10 
#     print(numero)
# prueba()    


# numero=10
# def prueba2():
#     numero=15
#     print(numero)
# prueba2()
# print(numero)



# #1mer paso

# def saludo_nombre(nombre):
#     saludos= print(f"hola {nombre}")
#     return saludos
# saludar=saludo_nombre("jesi")
# print(saludar)


# #2do paso
# def saludo_nombre(nombre):
#     saludos= print(f"hola {nombre}")
    
# saludar=saludo_nombre("jesi")
# print(saludar) 
# a=8
# b=12
# c=3
#1mer pso
# def numero_mayor(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:  
#      return c
# resultado= numero_mayor(8,12,3)        
# print(resultado) 



#2do paso
# def numero_mayor(a,b,c):
#    return max(a,b,c)
# resultado= numero_mayor(8,12,3)        
# print(resultado)     

#1mer paso
# def area_circulo(radio,pi):
#     return pi *(radio **2)
# resultado=area_circulo(10,3.14)
# print(resultado)

# #2do paso
# def area_circulo(radio,pi=3.14):
#     return pi *(radio **2)
# resultado=area_circulo(10)
# print(resultado)
# resultado=area_circulo(pi= 3.1417,radio=10)
# print(resultado)



#escribir una funcion que calcule la suma de dos numeros .
#si no se pasa el 2do numero su valor por default sera 10


# def suma (num1,num2=10):
#     return num1+num2
# resultado=suma(4)
# print(resultado)




#escribir una funcion que calcule el promedio de una lista de numeros,
#si no se proporciona una lista ,el valor por default sera una lista vacia()
def promedio(lista=[]):
    if len(lista)==0:
        return "la lista esta vacia"
    else:
     return sum(lista)/len(lista)
resutado=promedio([2,4,6,8])
print(resutado)    

