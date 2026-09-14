/*
 * SPDX-License-Identifier: MIT OR Apache-2.0
 *
 * Licensed under either the MIT license below or the Apache License, Version 2.0,
 * at your option. Apache license: https://www.apache.org/licenses/LICENSE-2.0
 *
 * MIT License
 *
 * Copyright (c) 2026 Schematic
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
 * associated documentation files (the "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
 * following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial
 * portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
 * EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
 * USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#ifndef SUPERTEST_H_INCLUDED
#define SUPERTEST_H_INCLUDED

#include <stdlib.h>

/* Source marker recognized by Schematic tooling. */
#define SUPERTEST

/* Reject this input by ending the current process successfully.
 * Evaluate one input per process. The condition is evaluated exactly once.
 */
#define SUPERTEST_ASSUME(condition) \
    do {                            \
        if (!(condition)) {         \
            exit(0);                \
        }                           \
    } while (0)

#endif
