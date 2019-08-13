#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
	int i = 0;
	int n;
	n=atoi(argv[1]); 
	printf("Hello world!\n");
	if (argc <2){
		printf("ingresa un numero\n"); 
		return(0); 
		}
	for (i=1;i<=n; i++){
		printf("\033[0;31m");
		printf("# %d FSE2020-1 CVCA HRP \n", i );
		printf("\033[0m");
	}
	return 0;
}
