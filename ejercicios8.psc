Algoritmo ejercicios8
	//Crea un programa que genere un arreglo de 10 números enteros aleatorios entre 1 y 100.
	//Luego, utiliza un bucle SI-Entonces para encontrar el número más grande en el arreglo
	Definir numerosArreglos Como Entero
	Dimension numerosArreglos[10]
	Para i= 0 Hasta 9 Con Paso 1 Hacer
		numerosArreglos[i]=azar(100)
		Imprimir  numerosArreglos[i]
		Si numerosArreglos[i] > numMayor Entonces
			numMayor=numerosArreglos[i]
			SiNo
				Si numerosArreglos[i]< numMenor Entonces
					numMenor= numerosArreglos[i]
				
				Fin Si
			Fin Si
		Fin Para
		Imprimir "el numero mayor es: " numMayor
FinAlgoritmo
