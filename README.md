# Supertest for C

Download [schematic.h](https://raw.githubusercontent.com/schematic-tech/supertest-c/v0.1.1/include/schematic.h) into your include directory.

```c
#include <assert.h>
#include <schematic.h>

SUPERTEST
void integer_division_is_bounded(int value, int divisor) {
    SUPERTEST_ASSUME(value >= 0 && divisor > 0);
    assert(value / divisor <= value);
}
```

See the [Getting Started Documentation](https://docs.schematic.tech/pup).

## License

This library is available under either MIT or Apache-2.0, at your option.
