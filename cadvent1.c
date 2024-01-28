
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
FILE* fptr;

int main() {
	fptr = fopen("input1.txt", "r");
	char* line = malloc(100);

	int total = 0;
	while (fgets(line, 100, fptr)) {
		int firstNum = 0;
		int lastNum = 0;
		for (int i = 0; i < strlen(line); i++) {
			char curChar = line[i];
			if (curChar >= '0' && curChar <= '9') {
				if (firstNum == 0) {
					firstNum = curChar - '0';
				}
				lastNum = curChar - '0';
			}
		}
		total += (10 * firstNum) + lastNum;
	}
	
	printf("\n%d", total);
	fclose(fptr);
}
