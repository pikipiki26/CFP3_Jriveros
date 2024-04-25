#crear una funcion que sume dos numeros


def suma (num1,num2):
    resutado = num1+num2
    return num1+num2
resutado_suma= suma(220,10)
print(resutado_suma)

#a la fincion anterior modificarla para que los numeros los pueda introducir el usuario.

# num1=(int(input(" ingrese un numero: ")))
# num2=(int(input("ingrese el otro numero")))
# RESULTADO= suma(num1,num2)
# print(F"LA SUMA DE {num1} Y {num2} ES: {RESULTADO} ")



#INCORPORA LA LOGUICA PARA QUE SOLICITE DE MANERA INDEFINIDA LA SUMA DE LOS DOS NUMEROS,HASTA QUE CONDICION CORTE EL CICLO
def suma(num1,num2):
    resultado= num1+ num2
    return resultado


def suma_bucle():
    resultado=[]
    total=0
    while True : 
        num1=int(input(" ingrse el primer valor (ingrese un numero nrgativo para salir; )"))
        if num1 < 0:
            print("usted esta saliendo del programa...")
            break
        num2=int(input("ingrse el segundo valor: "))
        resultado_suma=suma(num1,num2)
        resultado.append(resultado_suma)
        print(f"la suma de {num1} y {num2} es: {resultado_suma}")
    print(f"el resultado de la suma es: {sum(resultado)} ")
    for indice,resultado in enumerate(resultado,start=1):
        print(f"suma{indice}: {resultado}")    
suma_bucle()  

# #TODO:  enumerate ==> es una funcion en python que e utiliza para enumerar elementosde una secuencia (lista,tuplas,etc),mientras los recorre en un bucle. enumerate toma dos parametros: la secuencia que se quiere sumar y opcionalmente el indice inicial,devuelve un objeto enumerado que produce tuplas que  contiene un contador y un elemento de la secuenco
# frutas=["banana","pomelo","uva","mandarina"]
# for indice,frutas in enumerate(frutas,start=1):
#     print(f"{indice}: {frutas}: ")
#lo que se solicita es que guarden todos los resultados de la suma y mostrarlos al salir del bicle





