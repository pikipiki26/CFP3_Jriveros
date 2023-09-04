Algoritmo operacionNUM
	// SOLICITO EL 1ER num
	Imprimir "ingrese el 1er num: "
	// solicito el segundo num2
	Leer num1
	Imprimir "ingrese el 2do num: "
	Leer num2
	// calculos 
	suma = num1 + num2
	resta = num1 - num2
	multi = num1 * num2
	// muestro el resultado de las operaciones 
	Imprimir " la suma de los numeros es: " suma
	Imprimir " la resta de los numeros es: " resta 
	Imprimir " la multiplicacion de los numeros es: " multi
	Si num2 <> 0 Entonces 
		division= num1 / num2
		Imprimir "la division de los num es: " division
	SiNo
		
		Imprimir " no se puede dividir por 0: " 
	Fin Si
FinAlgoritmo
