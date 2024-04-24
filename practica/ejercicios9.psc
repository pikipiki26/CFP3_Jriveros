Algoritmo ejercicios9
	//Escribe un programa que permita al usuario ingresar un número
	//Luego, utiliza un bucle Mientras para verificar si ese número existe en un arreglo predefinido de 10 elementos
	//Si se encuentra, muestra un mensaje que diga "El número existe en el arreglo", de lo contrario, muestra "El número no existe en el arreglo"
	Definir numArreglo Como Entero
	Definir encontrado Como Logico
	encontrado= Falso
	Dimension numArreglo[10]
	Para i=0 Hasta 10-1 Con Paso 1 Hacer
		numArreglo[i]= azar(100)
		Imprimir numArreglo[i]
	Fin Para
	Escribir "ingrese un numero para buscar en el arreglo: "
	Leer numeroBuscado
	i=0
	Mientras i<=9 Hacer
		Si numArreglo[i]=numeroBuscado Entonces
			encontrado = Verdadero
		Fin Si
		i=i+1
	Fin Mientras
	Si eencontado Entonces
		Escribir "el numero ",numeroBuscado, " existe en el arreglo "
	SiNo
		Escribir "rl numero ", numeroBuscado, " no existe en el arreglo "
	Fin Si
	
FinAlgoritmo
