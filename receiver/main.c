#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	long time_taken;
	clock_t before = clock();
	int *p;
	char time[20];
	for (int i = 0; i < 10000; i++) {
		p = malloc(100000000 * sizeof(int));
		free(p);
	}
	time_taken = clock() - before;
	scanf("%s", time);
	printf("%s: Sample run for %f seconds.\n", time, (double) time_taken / CLOCKS_PER_SEC);
}
