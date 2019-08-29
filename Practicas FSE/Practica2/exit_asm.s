
@ Syscall defines
.equ SYSCALL_EXIT,     1


        .global main
	.func main
main:

        @================================
        bl exit
        @================================
exit:

	@ YOUR CODE HERE
	mov r0,#42
	mov r7,#SYSCALL_EXIT
	swi 0x0
