	.text
	.global main
	.func main
main:
	mov	r7,#4 @mueve un 4 a al regristro r7
	mov	r0,#1 @mueve un uno al registro 0
	ldr	r1,=message 
	mov 	r2,#19 @mueve un 19 constante al registro r2 tamano de la cadena
	svc	#0 
	mov	r7,#1 @mueve un 1 al registro r7
	mov	r0,#2 @mueve un cero al registro r0
	svc	#0
       .data

message: .ascii "FSE2020-1 is cool\n" @imprime la cadena codificada en ascii
