# lista1=[1,12,123]
# lista2=["bye","Ciao","Agur","Adieu"] 

# lista1.append("hola")
# lista1.append("1234")
# print(lista1)

# lista2.append("adios")
# lista2.append("1234")
# print(lista2)

# lista1.pop()
# lista3=lista1
# print(lista3)

# lista2.pop(0)
# lista2.pop(-1)
# lista4=lista2
# print(lista4)

# lista5 = lista3 + lista4
# print(lista5)


nombre= input("ingrese su nombre: ")
edad= int("ingrese su edad: ")
condicion=[nombre != "**** ",edad > 10 and edad < 18,len(nombre)<= 3 and len(nombre)<=10,edad*4 > 40]
print(condicion)
