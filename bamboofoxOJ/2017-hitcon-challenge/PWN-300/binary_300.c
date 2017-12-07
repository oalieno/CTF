#include<stdio.h>
#include<stdlib.h>

void useless(){
    system("");
}

int main(){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    char text[64];
    fgets(text,64,stdin);
    printf(text);
    fgets(text,64,stdin);
    printf(text);
    return 0;
}
