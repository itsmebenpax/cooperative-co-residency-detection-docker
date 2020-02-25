#include <stdio.h>
#include <stdlib.h>

int main()
{
	int sizefactor = 150000000;
	int* ptr = (int*) malloc(sizefactor * sizeof(int));
	for (int i = 0; i < 10000; i++) {
		for (int n = 0; n < sizefactor; n++) {
			ptr[n] = n+1;
		}
	}
	free(ptr);
}
