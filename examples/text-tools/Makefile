CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic
SCHEMATIC_INCLUDE ?= ../../include
CPPFLAGS += -Isrc -I$(SCHEMATIC_INCLUDE)

.PHONY: all clean
all: build/text.o build/collapse_spaces.o

build:
	mkdir -p build

build/text.o: src/text.c src/text.h | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

build/collapse_spaces.o: supertests/collapse_spaces.c src/text.h $(SCHEMATIC_INCLUDE)/schematic.h | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

clean:
	rm -rf build
