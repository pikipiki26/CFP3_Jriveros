
#TODO kwargs:es una sintaxis que se utiliza en python para aceptar un numero indefinido de argumentos de palabras calves en una funcion. la palabra clave **kwargs significa "keywork arguments"(argumento de palabras claves). estos argumentos se pasan en la afuncion como un diccionario, donde las claves son los nombres de argumentos y los valores son los valores asociados a esos argumentos.



# alumno= {
#     "mombre":"richar",
#     "apellido": "looza",
#     "edad":30
# }
# for i in alumno.keys:
#     print(i)

# def datos_alumnos(**kwargs):
#     pass
# datos_alumnos(nombre="jesi",apellido="riveros",edad=20)

def imprimir_info(**kwargs):
   for clave,valor in kwargs.items(): #el ciclo for itera sobre los diccionarios (con 3 tipos de valore "KEYS,VALUES E ITEMS")
    print(f"la calve es {clave} y su valor es {valor}")

imprimir_info(nombre="jesi" ,apellido="riveros" ,edad=25 ,direccion="pedraza 2525" ,cp=2010)

#TODO EJECICIO: ESCRIBIR UNA FUNCION LLAMADA "COMBINAR DICCIONARIO", QUE TOME VARIOS DICCIONARIOS  COMO ARGUMENTOS DE PALABRA CLAVE y DEVUELVA UN UNICO DICCIONARIO QUE CONTENGA LA COMBINACION DE TODOS LOS DICCIONARIOS PROPORCIONADO


def combinar_diccionario(**kwargs):
  resultado={}
  for diccionario in kwargs.values():
    resultado.update(diccionario)
    return resultado
dicc_1={"a":1,"b":2,"c":3}
dicc_2={"d":4,"e":5,"f":6}
resultado=combinar_diccionario(dic1=dicc_1,dic2=dicc_2)
print(resultado)


  

  