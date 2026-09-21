# Supertest for C

Download [schematic.h](https://raw.githubusercontent.com/schematic-tech/supertest-c/v0.1.1/include/schematic.h) into your include directory.

From the [text-tools example](examples/text-tools):

```c
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
```

See the [Getting Started Documentation](https://docs.schematic.tech/pup).

## Example

Try [text-tools](https://github.com/schematic-tech/supertest-c/tree/main/examples/text-tools). It includes a supertest
that finds a space-normalization bug.

## License

This library is available under either MIT or Apache-2.0, at your option.
