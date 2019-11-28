# Importing the Bluetooth Socket library
import bluetooth
# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)	# Using BCM numbering

todoC1=[22,27,17,10,9,11,5] #iniciamos toda la casa 1
todoC2=[24,23,18,25,12,16,20] #iniciamos toda la casa 2
PIR=21

GPIO.setup(PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(todoC1, GPIO.OUT)	# Declaring the pin 40 as output pin
GPIO.setup(todoC2, GPIO.OUT)	# Declaring the pin 40 as output pin
host = ""
port = 1	# Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
	server.bind((host, port))
	print("Bluetooth Binding Completed")
except:
	print("Bluetooth Binding Failed")
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address. 
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
AC1=0
AC2=0
state=0
try:
	time.sleep(0.2)
	while True:
		state=GPIO.input(PIR)
		data=client.recv(1024) # 1024 is the buffer size.
		#data=data.find('\n')
		# Receivng the data.
#		print(data)
	#	if state==1:
	#		GPIO.output(todoC1,(int(not a), int(b),int(c),int(d),int(e),int(f),int(g)))
	#		data=2
	#	else:
	#		data=client.recv(1024) # 1024 is the buffer size.
#	#		send_data=" "
	#		pass
		if int(data)==1:		#cocina casa 1
			GPIO.output(todoC1,(int(not a), int(b),int(c),int(d),int(e),int(f),int(g)))
		#	send_data = "Light On "
			a=int(not a)
#			time.sleep(5)
	#	else:
	#		pass
		elif int(data)==2:		#comedor casa 1
			GPIO.output(todoC1, (int(a),int(not b),int(c),int(d),int(e),int(f),int(g)))
			b=int(not b)
	#	else: 
	#		pass
		elif int(data)==3:		#sala casa 1
			GPIO.output(todoC1, (int(a),int(b),int(not c),int(d),int(e),int(f),int(g)))
			c=int(not c)
	#	else:
	#		pass
		elif int(data)==4:		#Escalera casa 1
			GPIO.output(todoC1, (int(a),int(b),int(c),int(not d),int(e),int(f),int(g)))
			d=int(not d)
	#	else:
	#		pass
		elif int(data)==5:		#cuarto 1 casa 1
			GPIO.output(todoC1, (int(a),int(b),int(c),int(d),int(not e),int(f),int(g)))
			e=int(not e)
	#	else:
	#		pass
		elif int(data)==6:		#bano
			GPIO.output(todoC1, (int(a),int(b),int(c),int(d),int(e),int(not f),int(g)))
			f=int(not f)
	#	else:
	#		pass
		elif int(data)==7:		#Cuarto 2 casa 2
			GPIO.output(todoC1, (int(a),int(b),int(c),int(d),int(e),int(f),int(not g)))
			g=int(not g)
	#	else:
		#	pass
		elif int(data)==8:		#Cocina casa 2
			GPIO.output(todoC2, (int(not h), int(i),int(j),int(k),int(l),int(m),int(n)))
			h=int(not h)
	#	else:
	#		pass
		elif int(data)==9:		#comedor casa 2
			GPIO.output(todoC2, (int(h),int(not i),int(j),int(k),int(l),int(m),int(n)))
			i=int(not i)
	#	else:
	#		pass
		elif int(data)==0:		#sala casa 2
			GPIO.output(todoC2, (int(h),int(i),int(not j),int(k),int(l),int(m),int(n)))
			j=int(not j)
	#	else:
	#		pass
		elif int(data)==10:		#Escalera casa 2
			GPIO.output(todoC2, (int(h),int(i),int(j),int(not k),int(l),int(m),int(n)))
			k=int(not k)
	#	else:
	#		pass
		elif int(data)==11:		#Cuarto 1 casa 2
			GPIO.output(todoC2, (int(h),int(i),int(j),int(k),int(not l),int(m),int(n)))
			l=int(not l)
	#	else:
	#		pass
		elif int(data)==12:		#bano 1 casa 2
			GPIO.output(todoC2, (int(h),int(i),int(j),int(k),int(l),int(not m),int(n)))
			m=int(not m)
	#	else:
	#		pass
		elif int(data)==13:		#cuarto 2 casa 2
			GPIO.output(todoC2, (int(h),int(i),int(j),int(k),int(l),int(m),int(not n)))
			n=int(not n)
	#	else:
		#	pass
		elif int(data)==14:		#toda casa 1
			GPIO.output(todoC1, int(not AC1))
			AC1=int(not AC1)
			a=AC1
			b=AC1
			c=AC1
			d=AC1
			e=AC1
			f=AC1
			g=AC1

	#	else:
	#		pass
		elif int(data)==15:		#planta baja casa 1
			GPIO.output(todoC1, (int(not o), int(not o), int(not o),0,0,0,0))
			o=int(not o)
			c=o
			b=o
			a=o

	#	else:
	#		pass
		elif int(data)==16:		#planta alta casa 1
			GPIO.output(todoC1, (0,0,0,0,int(not p), int(not p),int(not p)))
			p=int(not p)
			e=p
			f=p
			g=p
	#	else:
	#		pass
		elif int(data)==17:		#Toda casa 2 
			GPIO.output(todoC2, int(not AC2))
			AC2=int(not AC2)
			h=AC2
			i=AC2
			j=AC2
			k=AC2
			l=AC2
			m=AC2
			n=AC2
	#	else:
	#		pass
		elif int(data)==18:		#planta baja casa 2
			GPIO.output(todoC2, (int(not q), int(not q),int(not q),0,0,0,0))
			q=int(not q)
			h=q
			i=q
			j=q
#		else:
#			pass
		elif int(data)==19:		#planta alta casa 2
			GPIO.output(todoC2, (int(not r), int(not r),int(not r),0,0,0,0))
			r=int(not r)
			l=r
			m=r
			n=r
#		else:
#			pass
		elif int(data)==25 and state:
			print("hey, open", state)
			send_data="Hay alguien afuera"
			n=5
			for i in range(5):
				GPIO.output(todoC1, 1) 
				GPIO.output(todoC2, 1) 
				time.sleep(0.2)
				GPIO.output(todoC1, 0) 
				GPIO.output(todoC2, 0) 
				time.sleep(0.2)
				
				#GPIO.output(todoC1, 1) 
#			time.sleep(0.2)
			GPIO.output(todoC1, (a,b,c,d,e,f,g)) 
			GPIO.output(todoC2, (h,i,j,k,l,m,n)) 

		else: 
			print("no") 
			GPIO.output(todoC1, (a,b,c,d,e,f,g)) 
			GPIO.output(todoC2, (h,i,j,k,l,m,n)) 
			send_data=" " 
		#	time.sleep(0.1)

#			pass
		#elif int(data) ==2: send_data = "Light Off " 
		#	GPIO.output(led_pin, int(not n)) n=int(not n)
		#else:
		send_data = " "
		# Sending the data.
#		client.send(send_data)
#		data=0 gpio.cleanup()
except:
	# Making all the output pins LOW
	GPIO.cleanup()
	# Closing the client and server connection
	client.close()
	server.close()
