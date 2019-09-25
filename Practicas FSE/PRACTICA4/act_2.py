#Carvente Velasco Carlos Alberto
#Hernandez Romero Pompeyo 
import serial
from time import sleep
ser=serial.Serial('/dev/ttyS0') #open port
ser.baudrate=115200 ##set baudrate

while True: 
	datos=ser.read() #leer el puerto serial
#	datos=datos.replace(" ", "")
	sleep(0.03)		
	resto=ser.inWaiting() #revisa los datos por enviar 
	datos+=ser.read(resto)

	cadena=datos.split(',') #separando cada localidad de la lista por una coma en la entrada
#	cadena=cadena.replace(" ","")
#	if(str.isdigit(cadena[0])):
	
	if(int(cadena[0])<0 or int(cadena[0])>4095):
		print("El primer numero no entra en el rango\n")
		continue
	#if(str.isdigit(cadena[2]):)
#	if(len(cadena[2])>2):
#		print("bandera invalida")
#		print(len(cadena[2]))
	#	continue
	if(int(cadena[2])!=0 and int(cadena[2])!=1): 
		print("bandera invalida\n")
		continue
		
	float(cadena[3])
	#if(isintances(float(canena[3]),float)): 
	if(float(cadena[3])<0.0 or float(cadena[3])>3.3):
		print("el valor del voltaje es incorrecto\n")
		continue

	#else:
	#	print("el valor del voltaje es incorrecto\n") 

	print("Numero entero : "+ cadena[0])
	print("Iniciales: "+cadena[1])
	print("Bandera: "+cadena[2])
	print("Voltaje: "+ cadena[3])
	if '\n' in datos: 
		break
