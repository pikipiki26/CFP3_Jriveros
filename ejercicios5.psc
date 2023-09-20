Algoritmo ejercicios5
	//Pide al usuario dos números y muestra un mensaje que
	//indique cuál de los dos números es mayor, o si son iguales.
	Definir num1,num2 Como Entero
	Escribir "ingrese un numero sera proporcionado por el usuario"
	Leer num1,num2
	Si num1>num2  Entonces
		Imprimir num1," es el mayor"
	SiNo
		Si num1<num2 Entonces
			Imprimir num1," el menor"
		SiNo
			Imprimir " es igual"
		Fin Si
	Fin Si
FinAlgoritmo
