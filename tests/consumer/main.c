#include <schematic.h>

SUPERTEST
static void accepts_positive(int value) {
    SUPERTEST_ASSUME(value > 0);
}

int main(void) {
    accepts_positive(1);
    return 0;
}
