#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int filter(char* cmd){
        int r=0;
        printf("%s\n",cmd);
        r += strstr(cmd, "=")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "PATH")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "export")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "/")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "\\")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "`")!=0;
		printf("%d\n",r);
        r += strstr(cmd, "flag")!=0;
		printf("%d\n",r);
        return r;
}

extern char** environ;
void delete_env(){
        char** p;
        for(p=environ; *p; p++) memset(*p, 0, strlen(*p));
}

int main(int argc, char* argv[], char** envp){
        printf("getegid : %d\n",getegid());
        setregid(getegid(), -1);
        if(argc < 2) { return 0; }
        delete_env();
        putenv("PATH=/this_is_not_a_valid_path");
        if(filter(argv[1])) return 0;
        printf("%s\n", argv[1]);
        system( argv[1] );
        return 0;
}

