#Carvente Velasco Carlos Alberto
#Hernandez Romero Pompeyo
#Practica 4 Act 1
import serial

ser=serial.Serial ('/dev/ttyS0')
ser.baudrate=115200
for i in range(0,16):
	ser.write(str(i)+" :FSE 2020-1 Comunicacion UART RPi - FSE\n")
ser.close()
