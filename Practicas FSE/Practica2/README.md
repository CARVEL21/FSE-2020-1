Practica 2 Fundamentos de sistemas embebidos
Carvente Velasco Carlos Alberto
Hernández Romero Pompeyo

Práctica 2: Raspberry Pi: Lenguaje Ensamblador

Objetivo 
El alumno conocerá la programación en lenguaje ensamblador del procesador asociado a la tarjeta de desarrollo Raspberry Pi.

Respuestas breves y concisas. Ponga las respuestas en el archivo README usando un editor de texto.



------------------------------------Hello.s--------------------------x-------


	mov	r7,#4 @mueve un 4 a al regristro r7
	mov	r0,#1 @mueve un uno al registro 0
	ldr	r1,=message 
	mov r2,#19 @mueve un 19 constante al registro r2 tamano de la cadena
	svc	#0 
	mov	r7,#1 @mueve un 1 al registro r7
	mov	r0,#2 @mueve un cero al registro r0
	svc	#0   @cerramos canal
       .data

message: .ascii "FSE2020-1 is cool\n" @imprime la cadena codificada en ascii


Se abre el canal de salida estándar, después se recorrerá una cadena de caracteres que serán mostrados en la pantalla. Eventualmente cerramos el canal.



(a).Cuál es la diferencia entre las instrucciones swi 0x0,svc #0y, bx lr?
R: 
-swi: son interrupciones al sistema
-svc: supervisor del proceso de excepción de una llamada
-bx lr: returna a la función main

(b).A que se refiere la instrucción .balign 4 en el lenguaje ensamblador para ARM?

intrucción GNU de ".align 4" alinea los límites de los registros a 4.

(c).Cuántas instrucciones en lenguaje ensamblador hay para la arquitectura ARM11 y cuántos modos de direccionamiento hay (nombrelos)?


34 intrucciones:

ADC				Add with carry
ADD 			Add
AND 			AND
B 				Branch
BIC				Bit Clear
BL 				Branch with link
BX 				Branch and Exchange
CDP				Coprocessor Data Processing
CMN				Compare Negative
CMP 			Compare
EOR 			Exclusive OR
LDC				Load Coprecessor from memory
LDM 			Load multiple registers
LDR 			Load register from memory
MCR				Move CPU register to coprocessor register
MLA				Multiply Accumulate
MOV 			Move register or constant
MRC 			Move from coprocessor register from CPU register
MRS 			Move PSR status/flags to register
MSR 			Move Rregister to PSR status/flag
MUL 			Multiply
MVN				Move negative register
ORR				or
RSB 			Reverse Substract
RSC				Reverse Substract with Carry
SBC				Substract with carry
STC				Store coprocessor register to memory
STM				Store Multiple
STR 			Store register to memory
SUB 			Subtract
SWI 			Software Interrupt
SWP				Swap register with memory
TEQ				Test bitwise equality
TST 			Test bits


3 modos de direccioamiento:
Indirecto de registro
Indirecto de registro con desplazamiento constante
Indirecto de registro con desplazamiento por registro