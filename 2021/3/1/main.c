#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE_NAME "input.txt"

// File must be closed after
// Must return to beginning of file after (use rewind())
int getInputFileLines(FILE *inputFile) {
    int nrLines = 0;
    char tempChar;

    while ((tempChar = fgetc(inputFile)) != EOF) {
        if (tempChar == '\n') nrLines++;
    }

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

void getGammaRateStr(char* strGammaRate, const char* str, const int lineLength, const int nrLines) {
    strGammaRate[0] = '\0';

    for (int i = 0; i < lineLength; i++) {
        int nrOnes = 0;
        int nrZeros = 0;

        for (int j = 0; j < nrLines; j++) {
            if (str[i + (j * lineLength)] == '1') nrOnes++;
            else if (str[i + (j * lineLength)] == '0') nrZeros++;
        }

        strcat(strGammaRate, nrOnes > nrZeros ? "1" : "0");
    }
}

void getEpsilonRateStr(char* strEpsilonRate, const char* strGammaRate) {
    size_t i;

    for (i = 0; i < strlen(strGammaRate); i++) {
        switch (strGammaRate[i]) {
            case '0':
                strEpsilonRate[i] = '1';
                break;
            
            case '1':
                strEpsilonRate[i] = '0';
                break;
        }
    } 
    
    strEpsilonRate[i] = '\0';
}

int main() {
    char* str = NULL;

    FILE *inputFile = fopen(INPUT_FILE_NAME, "rt");

    if (inputFile == NULL) {
        fprintf(stderr, "ERROR: unable to read file %s.", INPUT_FILE_NAME);
        return -1;
    }

    int lineLength = getLengthOfLines(inputFile);
    int nrLines = getInputFileLines(inputFile);
    rewind(inputFile);

    str = malloc(lineLength * nrLines + 1);

    if (str == NULL) {
        fprintf(stderr, "ERROR: unable to allocate memory.");
        return -1;
    }

    readInputFromFile(inputFile, str);
    fclose(inputFile);

    char *strGammaRate = malloc((lineLength + 1) * sizeof(char));
    char *strEpsilonRate = malloc((lineLength + 1) * sizeof(char));
    getGammaRateStr(strGammaRate, str, lineLength, nrLines);
    getEpsilonRateStr(strEpsilonRate, strGammaRate);

    long gammaRate = strtol(strGammaRate, NULL, 2);
    long epsilonRate = strtol(strEpsilonRate, NULL, 2);

    printf("Result: %li\n", gammaRate * epsilonRate);

    free(strGammaRate);
    free(strEpsilonRate);
    free(str);
    return 0;
}