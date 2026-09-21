# Text tools

This example accompanies [Welcome to Pup](https://docs.schematic.tech/pup/).
It deliberately contains a bug: the loop skips only one extra space, so a run
of three spaces becomes two. The supertest checks that collapsing spaces again
leaves the result unchanged.

## Set up

With a C11 compiler and Make installed, run from the repository root:

```sh
cd examples/text-tools
make
```

The example uses the supertest library from this checkout.

## Check and fix

[Install the Schematic CLI and log in](https://docs.schematic.tech/pup/get-started/), then run
from this example directory:

```sh
sch link .
sch check .
```

The CLI links the containing `supertest-c` repository. The `.` in `sch check .`
selects only this example.

The check should fail. For example, `"a   b"` becomes `"a  b"` on the first call
and `"a b"` on the second. Pup may find a different counterexample.

Review and apply the proposed fix, then check again:

```sh
sch fix
sch check .
```

The CLI asks before applying the fix and whether to include uncommitted changes.
