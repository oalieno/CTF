#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//gcc bofe4sy.c -fno-stack-protector -o bofe4sy
void l33t(){
	puts("Congrat !");
	system("/bin/sh");
}


int main(){
	char buf[0x20];
	setvbuf(stdout,0,2,0);
	puts("Buffer overflow is e4sy");
	printf("Read your input:");
	read(0,buf,100);
	return 0 ;
}
