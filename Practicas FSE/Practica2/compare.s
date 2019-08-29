
.text
.global main

main:
        mov     r7, #4
        mov     r0,#1
        mov     r1, #9
        mov     r2, #9
        cmp     r1,r2
        beq     igual
        bgt     mayor
        blt     menor
        
igual:
 
                ldr r1, =m2
                mov     r2,#24
                b       texto   

menor:
                ldr r1,=m1   
                mov r2, #24
                b texto
mayor:
                ldr r1, =m3
                mov r2, #24
                                  
texto:

                svc     #0
                mov r7, #1
                mov r0, #0
                svc #0
.data
m2:
             .ascii "Los registro son iguales\n"
m1:
             .ascii "r1 es menor, r2 es mayor\n"
m3:
             .ascii "r1 es mayor, r2 es menor\n"
end:            bx      lr
                       
      

                        


