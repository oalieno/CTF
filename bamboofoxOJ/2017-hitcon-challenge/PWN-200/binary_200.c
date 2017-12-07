#include <stdio.h>
#include <stdlib.h>

void canary_protect_me(void){
    system("/bin/sh");
}

int main(void){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    char buf[40];
    gets(buf);
    printf(buf);
    gets(buf);
    return 0;
}
