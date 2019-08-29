LD = ld 
AS = as 
ASFLAGS_THUMB = -mthumb-interwork
LDFLAGS_THUMB = --thumb-entry=_start

CC = gcc
CFLAGS = -O2 -Wall
LFLAGS =


all:	exit_asm
all:	hello
all:	compare



exit_asm:	exit_asm.o
	$(LD) $(LDFLAGS) -o exit_asm exit_asm.o

hello:	hello.o
	$(LD) $(LDFLAGS) -o hello hello.o

compare:	compare.o
	$(LD) $(LDFLAGS) -o compare compare.o

exit_asm.o:	exit_asm.s
	$(AS) $(ASFLAGS) -o exit_asm.o exit_asm.s

hello.o:	hello.s
	$(AS) $(ASFhelloLAGS) -o hello.o hello.s

compare.o:	compare.s
	$(AS) $(ASFhelloLAGS) -o compare.o compare.s


submit:	exit_asm.s Makefile README
	tar -czvf P3_FSEsubmit.tar.gz exit_asm.s Makefile README

submit:	hello.s Makefile README
	tar -czvf P3_FSEsubmit.tar.gz hello.s Makefile README

submit:	compare.s Makefile README
	tar -czvf P3_FSEsubmit.tar.gz compare.s Makefile README

clean:	
	rm -f *~ *.o exit_asm
clean:	
	rm -f *~ *.o hello
clean:	
	rm -f *~ *.o compare
