#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <schematic.h>
/* The header must also be safe to include twice. */
#include <schematic.h>

static int calls = 0;

/* An assumption in a helper must stop the caller too. */
static int admitted_value(int value) {
    SUPERTEST_ASSUME((++calls, value > 0));
    return value;
}

SUPERTEST
static void accepts_positive_values(int value) {
    assert(admitted_value(value) == value);
    assert(calls == 1);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        return 64;
    }
    puts("entered");
    if (strcmp(argv[1], "true") == 0) {
        accepts_positive_values(1);
        /* The macro must act as one statement in an if/else. */
        if (1)
            SUPERTEST_ASSUME(1);
        else
            return 90;
        puts("continued");
        return 0;
    }
    if (strcmp(argv[1], "false") == 0) {
        accepts_positive_values(0);
        puts("continued");
        return 91;
    }
    if (strcmp(argv[1], "assertion") == 0) {
        SUPERTEST_ASSUME(1);
        assert(!"ordinary assertion failure");
        return 92;
    }
    return 64;
}
