Algoritmo ejercicios10
	//Crear un arreglo con n numeros,
	//ingresados por teclado y mostrar sus valores elevados al cuadrado
	Definir  numArreglo,dimencionArreglo Como Entero
	Imprimir "ingrese la dimencion del arreglo"
	Leer dimencionArreglo
	Dimension numArreglo[dimencionArreglo]
	Para i=0 Hasta dimencionArreglo-1 Con Paso 1 Hacer
		Imprimir "ingrese un  numero para el arreglo"
		Leer numArreglo[i]
	Fin Para
	
	Para i=0 Hasta dimencionArreglo-1 Con Paso 1 Hacer
		Imprimir numArreglo[i] ^ 2
		
	Fin Para
FinAlgoritmo
