# Text tools

This example accompanies [Welcome to Super](https://docs.schematic.tech/super/).
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

[Install the Super CLI and log in](https://docs.schematic.tech/super/get-started/), then run
from this example directory:

```sh
super link .
super check .
```

The CLI links the containing `supertest-c` repository. The `.` in `super check .`
selects only this example.

The check should fail. For example, `"a   b"` becomes `"a  b"` on the first call
and `"a b"` on the second. Super may find a different counterexample.

Review and apply the proposed fix, then check again:

```sh
super fix
super check .
```

The CLI asks before applying the fix and whether to include uncommitted changes.
