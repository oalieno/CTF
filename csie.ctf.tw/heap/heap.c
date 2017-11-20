#include <stdio.h>
#include <stdlib.h>

int main(){
	setvbuf(stdout,0,2,0);
	setvbuf(stdin,0,2,0);

	char *fastbin_chunk ;
	char *smallbin_chunk ;
	char *largebin_chunk ;
	char *temp ;
	fastbin_chunk = (char *)malloc(0x10) ; // fast bin chunk
	smallbin_chunk = (char *)malloc(0x80) ;// small bin chunk
	largebin_chunk = (char *)malloc(0x400); // large bin chunk	
	temp = (char *)malloc(0x10) ;// avoid merge to top


	printf("free a largebin_chunk %p\n",largebin_chunk);
	free(largebin_chunk); 	
	getchar();
	printf("put fastbin to fastbin %p\n",fastbin_chunk);
	free(fastbin_chunk);
	getchar();
	printf("put another fastbin to fastbin %p\n",temp);
	free(temp);
	getchar();
	printf("free the smallbin_chunk %p and merge with largebin_chunk %p\n",smallbin_chunk,largebin_chunk);
	free(smallbin_chunk);
	getchar();
	return 0;
}
