#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    // stage 1
    char * argv[101];
    for(int i = 0; i < 100; i++) {
        if(i == ((int)'A')) { argv[i] = "\x00"; }
        else if(i == ((int)'B')) { argv[i] = "\x20\x0a\x0d"; }
        else if(i == ((int)'C')) { argv[i] = 9999; }
        else { argv[i] = "A"; }
    } argv[100] = NULL;

    // stage 2
    int PIN[2], PERR[2]; pipe(PIN); pipe(PERR);
    write(PIN[1], "\x00\x0a\x00\xff", 4);
    write(PERR[1], "\x00\x0a\x02\xff", 4);

    // stage 3
    setenv("\xde\xad\xbe\xef", "\xca\xfe\xba\xbe", 1);

    // stage 4
    FILE *fp = fopen("\x0a", "w");
    write(fileno(fp), "\x00\x00\x00\x00", 4);
    fclose(fp);

    int pid = fork();
    if(pid == 0) {
        dup2(PIN[0], STDIN_FILENO);
        dup2(PERR[0], STDERR_FILENO);
        execv("./input", argv);
    }

    wait(NULL);

    return 0;
}
