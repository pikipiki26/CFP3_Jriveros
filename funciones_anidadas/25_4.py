#FUNCIONES ANIDADAS: las funciones pueden ser anidadas, es decir una funcion puede contener a otra funcion 

## EJEMPLO: operacones bancarias. deposito, retiro

def operacion():

    def deposito(cantidad,balance):
        return balance + cantidad
    def retiro(cantidad,balance):
        if cantidad<=balance:
            return balance - cantidad
        else:
            return None, "no tiene saldo suficiente para esta operacion"
        

#agregar a la funcion anterior la opcion de especificar el tipo de operacion que se desea realixar, 
#en el caso de no especificar una, tomar el valor deposito como defaull




def operacion(cantidad,balance, tipo="deposito" ):  #==> por defaull toma el valor 

    def deposito(cantidad,balance): #le sumo la cantidad de mi deposito con el balance 
        return balance + cantidad
    
    def retiro(cantidad,balance):
        if cantidad<=balance:
            return balance - cantidad
        else:
            return None, "no tiene saldo suficiente para esta operacion"
  
    if tipo=="deposito": #==>ACA LE DOY LAS  CONDICIONES PARA PODER REALIZAR LA OPERACION.
        return deposito(cantidad,balance)
    elif tipo== "retiro":
        return retiro(cantidad,balance)
    
tipo=input("INGRESE LA OPERACION (DEPOSITO-RETIRO)").lower() # TE TRANFORMA TODO EN MINUSCULA  Y ".UPPER()" TODO MASYUSCULA   
resultado= operacion(100,300,tipo) #==>especifico el tipo de parametro ,sino por defaull toma el valor del tipo de parameyros 
print(resultado)         

##escribir una funcion calcculadora que reciba 2 numeros y un caracter que indique el tipo de operaciones arealizar(+,-,*,/)la funcion  debe devolver el resultado dela operacion aritmetrica. utilizar funciones anidadas para implementar las operacione. la operaciones pordefault sera suma



def calculadora(num1,num2,operacion="+"):
    def suma(num1,num2):
        return num1+ num2
    
    def resta(num1,num2):
        return num1- num2   #HAGO MIS FUNCIONES ANIDADAS 
    
    def multiplicacion(num1,num2):
        return num1 *num2
    
    def divicion(num1,num2):
        return num1/num2
    
    if operacion=="+":
        return suma(num1,num2)
    elif operacion=="-":            
        return resta(num1,num2)
    elif operacion=="*":
        return multiplicacion(num1,num2)   #==>ACA LE DOY LAS  CONDICIONES PARA PODER REALIZAR LA OPERACION.
    elif operacion=="/":
        return divicion(num1,num2)
    else:
        return "SIGNO INVALIDO"
    
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))

resultado_suma=calculadora(num1,num2,"+")
resultado_resta=calculadora(num1,num2,"-")
resultado_multi=calculadora(num1,num2,"*")
resultado_divi=calculadora(num1,num2,"/")      #IACA IMPRIMO LOS RESULTADO DE MI OPERACION ATRAVES DE LAS CONDICIONALES "IF"
resultado_signo=calculadora(num1,num2,"%")
print(resultado_suma)
print(resultado_resta)
print(resultado_multi)
print(resultado_divi)
print(resultado_signo) #IMPRIME TODAS LAS OPERACIONES 


