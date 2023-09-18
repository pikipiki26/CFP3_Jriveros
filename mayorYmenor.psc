Algoritmo mayorYmenor8
	Definir  dimensionArreglo,valoresArreglos Como Entero
	Imprimir " ingresar la dimencion del arreglo: "
	Leer dimensonArreglo
	Dimension valoresArreglos[dimensonArreglo]
	Para i = 0 Hasta dimensonArreglo-1 Con Paso 1 Hacer
		Imprimir " ingresar el numero del arreglo: "
		Leer  valoresArreglos[i]
	FinPara
	

	mayor = valoresArreglos[0]
	menor = valoresArreglos[0]
	Para i= 1 Hasta dimensionArreglo-1 Con Paso 1 Hacer
		Si valoresArreglos[i] > mayor Entonces
			mayor = valoresArreglos[i]
		SiNo
			si valoresArreglos[i] < menor Entonces
			menor = valoresArreglos[i]

			Fin Si
		Fin Si
	Fin Para
	Imprimir " el numero mayor es: " mayor
	Imprimir " el numero menor es: " menor
	
FinAlgoritmo
