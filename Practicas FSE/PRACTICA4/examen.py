#Carvente Velasco Carlos Alberto
#Hernandez Romero Pompeyo 
import serial
from time import sleep
ser=serial.Serial('/dev/ttyS0') #open port
ser.baudrate=115200 ##set baudrate

while True: 
	datos=ser.read() #leer el puerto serial
#	datos=datos.replace(" ", "")
#	datos=datos.replace("\x00", "")
	sleep(0.03)		
	resto=ser.inWaiting() #revisa los datos por enviar 
	datos+=ser.read(resto)

	cadena=datos.split(',') #separando cada localidad de la lista por una coma en la entrada
#	continue
#	ser.write("hola\n")
	ser.write('Voltaje: '+cadena[0]+"[mV] Kelvin = "+cadena[1]+"[K] Celcius= "+cadena[2]+"[C]\n")
	voltaje="voltaje: {}"
	kelvin="kelvin:{} "
	celcius="Celcius: {}"
	print(voltaje.format(cadena[0])+" "+kelvin.format(cadena[1])+" "+celcius.format(cadena[2]))
#	if len(cadena)==0: 
#		break
#	continue
ser.close()
