Algoritmo practica7
	//Se solicita crear un algoritmo que pida numeros por teclado
	//y los almacene en 3 arreglos diferentes y mostrar en un cuarto arreglo el promedio.
	//La dimensión debe ser dinámica, es decir, el usuario la debe determinar.
	Definir arreglo1,arreglo2,arreglo3,sumaDeArreglos Como Entero

	Imprimir "ingrese la dimension del arreglo: "
	leer dimensionArreglo
	
	Dimension arreglo1[dimensionArreglo], arreglo2[dimensionArreglo], arreglo3[dimensionArreglo], sumaDeArreglos[dimensionArreglo]
	
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "ingrese un numero de arreglo 1 sera proporcionado por el usario: "
		Leer arreglo1[i]
		Imprimir "ingrese un numero de arreglo 2 sera proporcionado por el usario: "
		Leer arreglo2[i]
		Imprimir "ingrese un numero de arreglo 3 sera proporcionado por el usario: "
		Leer arreglo3[i]
		
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo-1 Con Paso 1 Hacer
		Imprimir "numeros de arreglo 1: " arreglo1[i] 
		Imprimir "numeros de arreglo 2: " arreglo2[i]
		Imprimir "numeros de arreglo 3: " arreglo3[i]
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo-1 Con Paso 1 Hacer
		//sumArreglo  = arreglo1[i] + arreglo2[i] + arreglo3[i] 
		sumaDeArreglos[i] = (arreglo1[i] + arreglo2[i] + arreglo3[i] ) / dimensionArreglo
		Imprimir "promedio de arreglos: " sumaDeArreglos[i]
	Fin Para
		
		

	
FinAlgoritmo
