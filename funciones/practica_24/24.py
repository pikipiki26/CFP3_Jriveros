#print("hola mundo")
 
#OPERADOR TERNARIO


#cual seria la logica para evaluar un numero y si es mayor o igial a 6 mostrar el mensaje "verde" y sino mostrar el mensaje "rojo"

#variables
#en python tenemoos la posbilidad de declarar variables vacias.es decir con valor "none"


#FORMA1
nota= 8
color=None
if nota >=6:
    print("verde")
else:
    print("rojo")



#operador ternario==> nos permite evaluar una condicion de manera abreviada

#FORMA2
nota=8
color= "verde" if nota >=6 else "rojo"
print(nota,color)  

#Dado un numero entero,imprimir es "par" si el numero es par
#y es "impar" si es impar


#TERNARIO
num= int(input("ingrese un numero: "))
resultado= "es par" if num % 2==0 else"es impar"
print(resultado)

#DADO 2 NUMEROS ENTEROS A Y B IMPRIMIR "A ES MSYOR" SI ES MAYOR QUE B
#"B  ES MAYOR", SI B MAYOR QUE A, SI SON IGUALES ,MOSTRAR EL MENSAJE "AMBOS SON IGUALES"

#forma tradicional
a=2
b=20
if a>b :
    print("A es mayor") 
elif b>a :
    print("B es mayor")
else:  
    print("ambos son iguales")

#forma operador alternario
a=2
b=36
resultado= "A es mayor" if a>b else("B es mayor"if b>a else "son igaule")
print(resultado)


    




