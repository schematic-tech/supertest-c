#include <assert.h>
#include <schematic.h>
#include <stdlib.h>
#include <string.h>
#include "text.h"

SUPERTEST
void collapsing_spaces_again_changes_nothing(const char *text) {
    SUPERTEST_ASSUME(text != NULL);
    char *once = collapse_spaces(text);
    char *twice = collapse_spaces(once);
    int unchanged = strcmp(twice, once) == 0;

    free(once);
    free(twice);
    assert(unchanged);
}
