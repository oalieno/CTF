#include <unistd.h>
#include <stdio.h>
#include "mysandbox.h"

char shellcode[200];

int main(){
	setvbuf(stdout,0,2,0);
	my_sandbox();	
	printf("Give me your shellcode:");
	read(0,shellcode,200);
	(*(void(*)())shellcode)();
}
