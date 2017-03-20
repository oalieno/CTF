/**
 * @file adrVM.cpp
 * @author aaaddress1@gmail.com
 * @date 2017/02/16
 **/
#include <stdio.h>
#include <cstdlib>
#define strcmp(arr1, arr2) ({ int p = 0; for(;*(arr1+p)&&*(arr2+p)&&(*(arr1+p)==*(arr2+p));p++); (!*(arr1+p))&&(!*(arr2+p)); })
#define strlen(arr) ({ char *tp = arr; while(*tp++); (int)(tp-arr-1); })
#define strcpy(dest, src) ({ int p = 0; for(;*(src+p);*(dest+p)=*(src+p), p++); })
#define printExit(msg) ({ puts(msg); exit(0); })

void loadFlag(char *flag) {
	FILE *fflag = fopen("flag_exam3.txt", "r");
	if (!fflag)
		printExit("cannot find flag file.");
	fscanf(fflag, "%s", flag);
}

int main(int argc, char **argv) {
	char flag[64]; /* flag type: TDOH{...XXXXXXXXXXXXXXXX...} */
	char *code = new char[0x100];
	size_t trap = 0x00524441, f = (size_t)flag;
	char *VM = (char *)&trap;

	if (argc == 1) printExit("[error] you must give a param as input.");
	if (strlen(argv[1]) > 0xff) printExit("[error] your code too long.");
	
	strcpy(code, argv[1]);
	
	/* ADR VM Engine */
	printf("[info] input code: %s\n\n", code);
	{
		for (;*code; code++) {
			switch (*code) {
				case '0': VM++; break;
				case '1': VM--; break;
				case '2': (*VM)++; break;
				case '3': (*VM)--; break;
				case '$':
					puts("[info] entering adr vm debug mode.");
					printf("\t- current trap: %s\n", (&trap));
					printf("\t- flag pointer: %p\n", (char *)f);
					printf("\t- VM pointer: %p\n\n", VM);
					break;
				default: 
					printf("[warning] VM doesn't support opcode %c !\n\n", *code);
					break;
			}
		}
		if (strcmp((char*)&trap, "BEEF")) {
			puts("[info] you found the trap!");
			loadFlag(flag);
		}
	}
	printf("VM resault: %s\n", (char *)VM);
	return 0;
}
