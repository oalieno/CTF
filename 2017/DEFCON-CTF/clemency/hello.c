#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned char lifegoals[] = {
229,
187,
190,
228,
185,
135,
228,
185,
154,
228,
185,
154,
227,
132,
150,
32,
229,
177,
177,
227,
132,
150,
229,
176,
186,
228,
185,
154,
225,
151,
170,
33
};

int lifegoals_len = sizeof(lifegoals);

int ReadUntil(char *Buf, int MaxLen, int DelimChar) {
        int len;
        int TotalLen = 0;
        int i;
	char Delim = DelimChar;
        if (!Buf) {
                return(0);
        }
        memset(Buf, 0, MaxLen);
        while (TotalLen < MaxLen) {
                len = read(Buf+TotalLen, 1);
                if (len == -1) {
                        return(0);
                }
                if (len == 0) {
                        wait();
                        continue;
                }
                if (Buf[TotalLen] == Delim) {
                        Buf[TotalLen] = '\0';
                        return(TotalLen);
                }
                TotalLen += 1;
                if (TotalLen >= MaxLen) {
                        Buf[MaxLen-1] = '\0';
                        return(MaxLen-1);
                }
        }
        return(TotalLen);
}

int main() {
	int i;
	unsigned int num;
	char buf[10];

        for (i = 0; i < 214; i++) {
		ReadUntil(buf, sizeof(buf), '\n');
		num = atoi(buf);

                printf("%d %d %d\n", i, num, lifegoals[i]);

                if (num != lifegoals[i]) exit(1);
        }

        puts(lifegoals);
	fflush(stdout);
}
