CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic
CPPFLAGS += -Iinclude
PYTHON ?= python3

.PHONY: all test clean

all: test

build/authoring: tests/authoring.c include/schematic.h
	mkdir -p build
	$(CC) $(CPPFLAGS) $(CFLAGS) tests/authoring.c -o $@

test: build/authoring
	$(PYTHON) tests/test_authoring.py -v

clean:
	rm -rf build
