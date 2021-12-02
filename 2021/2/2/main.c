#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE_NAME "input.txt"

void executeInstruction(const char *instruction, const int steps, int *horizontalPosition, int *depth, int *aim) {
    if (strcmp("forward", instruction) == 0) {
        *horizontalPosition += steps;
        *depth += steps * (*aim);
    } else if (strcmp("up", instruction) == 0) {
        *aim -= steps;
    } else if (strcmp("down", instruction) == 0) {
        *aim += steps;
    } else {
        fprintf(stderr, "ERROR: Invalid instruction <%s>.", instruction);
    }
}

void readInputCourseFromTxt(int *horizontalPosition, int *depth, int *aim, char *fileName) {
    FILE *inputFile = NULL;

    inputFile = fopen(fileName, "rt");

    if (inputFile == NULL) {
        fprintf(stderr, "ERROR: unable to read file %s.", fileName);
        return;
    }
    
    int intBuffer;
    char strBuffer[64];

    while (fscanf(inputFile, "%s %i", strBuffer, &intBuffer) == 2) {
        executeInstruction(strBuffer, intBuffer, horizontalPosition, depth, aim);
    }

    fclose(inputFile);
}

inline int finalCalculation(const int a, const int b) { return a * b; }

int main() {
    int horizontalPosition = 0;
    int depth = 0;
    int aim = 0;

    readInputCourseFromTxt(&horizontalPosition, &depth, &aim, INPUT_FILE_NAME);

    int result = finalCalculation(horizontalPosition, depth);
    printf("Result: %i\n", result);

    return 0;
}