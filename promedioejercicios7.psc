Algoritmo EJERCICIO_1
	// DEFINIR EL TIPO DE NUESTRO ARREGLO
	Definir calificaciones Como Entero
	Imprimir " cuantas notas deseas agregar?: "
	Leer  valor
	Dimension calificaciones[valor]
	Para i= 0 Hasta valor-1 Con Paso 1 Hacer
		Imprimir " ingrese las notas del alumno: "
		Leer calificaciones[i]
		sumaNotas=sumaNotas+ calificaciones[i]
		promedio=sumaNotas / valor 
	Fin Para
	Imprimir " el promedio del alumno es: " promedio
	
FinAlgoritmo
