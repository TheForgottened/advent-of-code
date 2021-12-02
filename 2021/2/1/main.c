#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE_NAME "input.txt"

void executeInstruction(const char *instruction, const int steps, int *horizontalPosition, int *depth) {
    if (strcmp("forward", instruction) == 0) {
        *horizontalPosition += steps;
    } else if (strcmp("up", instruction) == 0) {
        *depth -= steps;
    } else if (strcmp("down", instruction) == 0) {
        *depth += steps;
    } else {
        fprintf(stderr, "ERROR: Invalid instruction <%s>.", instruction);
    }
}

int readInputCourseFromTxt(int *horizontalPosition, int *depth, char *fileName) {
    int size = 0;
    FILE *inputFile = NULL;

    inputFile = fopen(fileName, "rt");

    if (inputFile == NULL) {
        fprintf(stderr, "ERROR: unable to read file %s.", fileName);
        return -1;
    }
    
    int intBuffer;
    char strBuffer[64];

    while (fscanf(inputFile, "%s %i", strBuffer, &intBuffer) == 2) {
        executeInstruction(strBuffer, intBuffer, horizontalPosition, depth);
    }

    fclose(inputFile);
    return size;
}

inline int finalCalculation(const int a, const int b) { return a * b; }

int main() {
    int horizontalPosition = 0;
    int depth = 0;

    readInputCourseFromTxt(&horizontalPosition, &depth, INPUT_FILE_NAME);

    int result = finalCalculation(horizontalPosition, depth);
    printf("Result: %i\n", result);

    return 0;
}