#include<stdio.h>
#include<stdlib.h>

int main(){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    char text[40];
    int to_be_overflowed;
    gets(text);
    if(to_be_overflowed == 0xABCD1234) system("/bin/sh");
    else puts("DO YOU KNOW HOW TO BOF?");
    return 0;
}
