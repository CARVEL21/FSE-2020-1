#Carvente Velasco Carlos Alberto
#Hernandez Romero Pompeyo
import csv
import sys

def main():
	a=int(sys.argv[2])
	name=str(sys.argv[1])
	cadena=[]
	with open('/media/pi'+name, mode='w') as p_file: #raspberry
	#with open(name, mode='w') as p_file: #windows
		p_write=csv.writer(p_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range (a+1):
			cadena=[str(i), 'hola usb', 'dato '+str(i)]
			p_write.writerow(cadena)
main()