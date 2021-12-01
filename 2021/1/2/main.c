#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE_NAME "input.txt"

void addIntToArray(int **arrayPointer, int *size, const int newNumber) {
  int *tempArray = realloc(*arrayPointer, (*size + 1) * sizeof(int));

  if (tempArray == NULL) {
    fprintf(stderr, "ERROR: unable to allocate memory for array of ints.");
    return;
  }

  *arrayPointer = tempArray;
  (*arrayPointer)[*size] = newNumber;
  (*size)++;
}

int readInputIntFromTxt(int **arrayPointer, char *fileName) {
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

int nrTimeDepthIncreases(const int *array, const int size, const int window) {
  int number = 0;

  for (int i = 0; i < size - window; i++) {
    if (array[i] < array[i + window])
      number++;
  }

  return number;
}

#include <sys/time.h>
int main() {

  struct timeval timer[2];
  gettimeofday(&timer[0], NULL);

  int *array = NULL;
  int arraySize;

  arraySize = readInputIntFromTxt(&array, INPUT_FILE_NAME);

  int nrDepthIncreases = nrTimeDepthIncreases(array, arraySize, 3);
  printf("Number of times a depth measurement increases is %i.\n",
         nrDepthIncreases);

  free(array);

  gettimeofday(&timer[1], NULL);

  printf("time taken: %ld μs\n", timer[1].tv_usec - timer[0].tv_usec);
  return 0;
}