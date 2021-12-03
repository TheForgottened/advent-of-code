#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE_NAME "input.txt"

void removeElementsFromString(char* str, const int index, const int n) {
    memmove(
        str + (index * sizeof(char)), 
        str + ((index + n) * sizeof(char)), 
        strlen(str + ((index + n) * sizeof(char))) + 1
    );
}

// File must be closed after
// Must return to beginning of file after (use rewind())
int getInputFileLines(FILE *inputFile, const int lineLength) {
    int nrLines = 0;
    int size = lineLength + 3; // \r\n\0
    char* tempStr = malloc(size * sizeof(char));

    while (fgets(tempStr, size, inputFile) != NULL) nrLines++;

    free(tempStr);
    return nrLines;
}

// File must be closed after
// Must return to beginning of file after (use rewind())
int getLengthOfLines(FILE *inputFile) {
    char strBuffer[64];

    fscanf(inputFile, "%s", strBuffer);

    return strlen(strBuffer);
}

int readInputFromFile(FILE *inputFile, char *str) {
    int size = 0; 
    char tempChar;
    int i = 0;

    while (fscanf(inputFile, "%c", &tempChar) == 1) {
        if (tempChar == '\n' || tempChar == 13) continue;
        
        str[i] = tempChar;
        i++;
    }

    str[i] = '\0';

    return size;
}

char* getOxygenGeneratorRating(const char* str, const int lineLength, int nrLines) {
    char* tempStr = malloc((strlen(str) + 1) * sizeof(char));
    memcpy(tempStr, str, (strlen(str) + 1) * sizeof(char));

    for (int i = 0; i < lineLength; i++) {
        int nrOnes = 0;
        int nrZeros = 0;

        int j;
        for (j = 0; j < nrLines; j++) {
            if (tempStr[i + (j * lineLength)] == '1') nrOnes++;
            else if (tempStr[i + (j * lineLength)] == '0') nrZeros++;
        }

        char forbidden = nrZeros <= nrOnes ? '0' : '1';

        j = 0;
        while (j < nrLines) {
            if (tempStr[i + (j * lineLength)] != forbidden) {
                j++;
                continue;
            }

            removeElementsFromString(tempStr, j * lineLength, lineLength);
            nrLines--;
        }

        if (strlen(tempStr) == lineLength) break;
    }

    return tempStr;
}

char* getCO2ScrubberRating(const char* str, const int lineLength, int nrLines) {
    char* tempStr = malloc((strlen(str) + 1) * sizeof(char));
    memcpy(tempStr, str, (strlen(str) + 1) * sizeof(char));

    for (int i = 0; i < lineLength; i++) {
        int nrOnes = 0;
        int nrZeros = 0;

        int j;
        for (j = 0; j < nrLines; j++) {
            if (tempStr[i + (j * lineLength)] == '1') nrOnes++;
            else if (tempStr[i + (j * lineLength)] == '0') nrZeros++;
        }

        char forbidden = nrZeros <= nrOnes ? '1' : '0';

        j = 0;
        while (j < nrLines) {
            if (tempStr[i + (j * lineLength)] != forbidden) {
                j++;
                continue;
            }

            removeElementsFromString(tempStr, j * lineLength, lineLength);
            nrLines--;
        }

        if (strlen(tempStr) == lineLength) break;
    }

    return tempStr;
}

int main() {
    char* str = NULL;

    FILE *inputFile = fopen(INPUT_FILE_NAME, "rt");

    if (inputFile == NULL) {
        fprintf(stderr, "ERROR: unable to read file %s.", INPUT_FILE_NAME);
        return -1;
    }

    int lineLength = getLengthOfLines(inputFile);
    int nrLines = getInputFileLines(inputFile, lineLength);
    rewind(inputFile);

    str = malloc(lineLength * nrLines + 1);

    if (str == NULL) {
        fprintf(stderr, "ERROR: unable to allocate memory.");
        return -1;
    }

    readInputFromFile(inputFile, str);
    fclose(inputFile);

    char* strOxygenGeneratorRating = getOxygenGeneratorRating(str, lineLength, nrLines);
    char* strCO2ScrubberRating = getCO2ScrubberRating(str, lineLength, nrLines);
    long oxygenGeneratorRating = strtol(strOxygenGeneratorRating, NULL, 2);
    long co2ScrubberRating = strtol(strCO2ScrubberRating, NULL, 2);

    printf("Result: %li\n", oxygenGeneratorRating * co2ScrubberRating);

    free(str);
    free(strOxygenGeneratorRating);
    free(strCO2ScrubberRating);
    return 0;
}