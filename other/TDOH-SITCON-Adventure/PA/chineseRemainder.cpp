/**
 * @file chineseRemainder.cpp
 * @author aaaddress1@gmail.com
 * @date 2017/02/16
 **/
#include <stdio.h>
#include <cstdlib>
#define strlen(arr) ({ char *tp = arr; while(*tp++); (int)(tp-arr-1); })
#define printExit(msg) ({ puts(msg); exit(0); })

char privKey[] = "/*´∇｀*/"; /* you don't my private key :P */
const int privKeyLen = 4;

char flag[64]; /* flag type: TDOH{...XXXXXXXXXXXXXXXX...} */
char *publKey;
char *secret;

int main(void) {
	FILE *fflag = fopen("flag.txt", "r");
	FILE *fpubli = fopen("publi.txt", "w");
	FILE *fsecret = fopen("secret.txt", "w");

	if (!fflag || !fpubli || !fsecret)
		printExit("cannot find flag, public key, or secret file.");

	fscanf(fflag, "%s", flag);
	publKey = new char[strlen(flag) + 1];
	secret = new char[strlen(flag) + 1];

	for(int i = 0; i < strlen(flag); i++) {
		publKey[i] = flag[i]/privKey[i % privKeyLen];
		secret[i] = flag[i] - (publKey[i] * privKey[i % privKeyLen]);
		fprintf(fpubli, "%02x", publKey[i]);
		fprintf(fsecret, "%02x", secret[i]);
	}
	puts("!! the remainder is CHINESE !!");
	return 0;
}
