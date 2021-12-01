#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE_NAME "input.txt"

void addIntToArray(int** arrayPointer, int* size, const int newNumber) {
    int* tempArray = realloc(*arrayPointer, (*size + 1) * sizeof(int));

    if (tempArray == NULL) {
        fprintf(stderr, "ERROR: unable to allocate memory for array of ints.");
        return;
    }

    *arrayPointer = tempArray;
    (*arrayPointer)[*size] = newNumber;
    (*size)++;
}

int readInputIntFromTxt(int** arrayPointer, char* fileName) {
    int size = 0;
    FILE *inputFile = NULL;

    inputFile = fopen(fileName, "rt");

    if (inputFile == NULL) {
        fprintf(stderr, "ERROR: unable to read file %s.", fileName);
        return -1;
    }
    
    int temp;

    while (fscanf(inputFile, "%i", &temp) == 1) {
        addIntToArray(arrayPointer, &size, temp);
    }

    fclose(inputFile);
    return size;
}

int nrTimesDepthIncreases(const int* array, const int size) {
    int number = 0;

    for (int i = 0; i < size - 2; i++) {
        if (array[i] < array[i + 1]) number++;
    }

    return number;
}

int main() {
    int* array = NULL;
    int arraySize;

    arraySize = readInputIntFromTxt(&array, INPUT_FILE_NAME);

    int nrDepthIncreases = nrTimesDepthIncreases(array, arraySize);
    printf("Number of times a depth measurement increases is %i.\n", nrDepthIncreases);

    free(array);
    return 0;
}