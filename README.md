# Supertest for C

Add this repository's `include/` directory to your compiler include path:

```c
#include <assert.h>
#include <schematic.h>

SUPERTEST
void integer_division_is_bounded(int value, int divisor) {
    SUPERTEST_ASSUME(value >= 0 && divisor > 0);
    assert(value / divisor <= value);
}
```

`SUPERTEST` is a passive source marker. C has no namespace mechanism, so its flat
public APIs are `SUPERTEST` and `SUPERTEST_ASSUME(condition)`.

A true assumption continues and the expression is evaluated once. A false assumption
calls `exit(0)`, ending the entire hosted process successfully, even inside a helper.
Run one input per process. C exit handlers execute as usual. Assertions remain ordinary
assertions; build without `NDEBUG` when exercising them.

This differs from the old header's early return and the current website description.
Keep top-level supertests `void` for current Pup discovery. The header supplies authoring
primitives; it does not generate inputs or check all values by itself.

```sh
make test
make clean test CC=clang
```

Requires a C11 compiler, Make, and Python 3 for subprocess checks. Adapted from `schematic-tech/schematic-supertests` at
`b6ccba3b5e0d42ea2846d0476eeb9496afb4a7f4`.

## Distribution

Copy `include/schematic.h` directly, or use the CMake package:

```cmake
find_package(SchematicSupertest CONFIG REQUIRED)
target_link_libraries(my_tests PRIVATE schematic::supertest)
```

To install it locally:

```sh
cmake -S . -B build/cmake -DCMAKE_INSTALL_PREFIX=/your/prefix
cmake --install build/cmake
```

Vendored checkouts work with `add_subdirectory(path/to/supertest-c)` and the same
`schematic::supertest` target. `FetchContent` can download a tagged checkout or a
release archive; use the published `SHA256SUMS` when setting `URL_HASH`.

For vcpkg, either use this checkout's `ports/` as `--overlay-ports`, or download
the standalone release overlay ZIP. For Conan 2, run `conan create .` from this
checkout. The CMake package and both package-manager integrations remain header-only.
See [release setup and download URLs](RELEASING.md).

## License

This interoperability library is available under either [MIT](LICENSE-MIT) or
[Apache-2.0](LICENSE-APACHE), at your option.
