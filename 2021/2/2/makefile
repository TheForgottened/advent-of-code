# Defines the C compiler
CC := gcc

# Protection for stack-smashing attack
STACK := -fstack-protector-all -Wstack-protector

# Specifies to GCC the required warnings
WARNS := -Wall -Wextra -pedantic # -pedantic warns on language standards

# Debug flags
DEBUG := -g -fsanitize=address 

# Flags for compiling
CFLAGS := -O3 $(STACK) $(WARNS)

# Source code file extension
SRCEXT := c

# Binary name
BINARY := a.out

# %.o file names
NAMES := $(notdir $(basename $(wildcard *.$(SRCEXT))))
OBJECTS :=$(patsubst %,%.o,$(NAMES))

#
# Compilation Rules
#

default: all

# Help message
help:
	@echo "Advent of Code 2021 - day 1, part 2"
	@echo "    all		- Compiles and generates binary files"
	@echo "    clean    - Clean the project by removing binaries"
	@echo "    help     - Prints a help message with target rules"

all: $(OBJECTS)
	$(CC) -o $(BINARY) $+ $(CFLAGS) $(LIBS)
	@echo -en "\n--\nBinary file placed at $(BINARY)\n"

# Rule to compile with debug flags
debug: $(OBJECTS)
	$(CC) -o $(BINARY) $+ $(CFLAGS) $(DEBUG) $(LIBS)
	@echo -en "\n--\nBinary file placed at $(BINARY)\n"

%.o: %.$(SRCEXT)
	$(CC) -c $^ -o $@ $(CFLAGS) $(LIBS)

# Rule for cleaning the project
clean:
	@rm -rvf *.out *.o;