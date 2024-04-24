Algoritmo practica6
	//Se solicita crear un programa que pida 10 numeros por teclado
	//y mientras se vayan ingresando los numeros
	//estos sean ordenados en un arreglo de 10 elementos en orden ascendente. 
	Definir i,f,ff,vector, temp Como Entero
	Dimension vector[10]
	temp=0
	f=0
	ff=0
	Para i=0 Hasta  10-1 Con Paso 1 Hacer
		Imprimir "ingrese el numero",i +1,"="
		Leer vector[i]
		Para f=0 Hasta i Con Paso 1 Hacer
			Para ff=f Hasta i Con Paso 1 Hacer
				Si vector[f] > vector[ff]  Entonces
					temp=vector[f]
					vector[f]=vector[ff]
					vector[ff]= temp
				Fin Si
			Fin Para
		
		Fin Para
	Fin Para
	//imprimo mi lista ordenada
	Para i=0 Hasta 10-1 Con Paso 1 Hacer
		Imprimir Sin Saltar " " vector[i]
	Fin Para
	
FinAlgoritmo
