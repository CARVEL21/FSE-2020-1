Practica 4 Fundamentos de sistemas embebidos 
Carvente Velasco Carlos Alberto
Hernández Romero Pompeyo

Raspberry Pi: Puerto serie y módulo UART

Objetivo: El alumno conocerá la configuración, la programación y el uso del módulo UART (Universal Asynchronous Receiver Transmitter) para implementar comunicaciones de tipo serial, particularmente bajo el estándar RS-232.

Descripción: consta de dos actividades


-Primera Actividad
	Desarrolle un programa en C o Python que escriba de la Raspberry a la PC, la siguiente cadena, i = 0, . . . , 15 veces
	0: FSE 2020-1 Comunicacion UART RPi - FSE
	.
	15: FSE 2020-1 Comunicacion UART RPi - FSE

-Segunda Actividad
	Desarrolle un programa en C o Python que sea capaz de recibir datos provenientes de la PC hacia la Raspberry Pi. LA cadena que enviar ́a desde la PC deberá tener la estructura siguiente:
	numero entero,iniciales,numero binario,numero decimal
	en donde numero entero es número entre 0 y 4095, iniciales es una cadena con las iniciales de los nombres de
	cada equipo, numero binario es un 0  ó 1, y numero decimal es un número entre 0.0 y 3.3.
	Una vez recibida la cadena, el programa deberá separar cada campo de la trama, e imprimirlos en la terminal
	minicom con el siguiente formato:

	Número entero: xxxx 
	Iniciales: xxxx 
	Bandera: x
	Voltaje: xxx
	
	video tutorial https://www.youtube.com/watch?v=eCNbklyQ0XQ&feature=youtu.be
