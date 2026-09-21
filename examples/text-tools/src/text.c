#include "text.h"
#include <stdlib.h>
#include <string.h>

char *collapse_spaces(const char *text) {
    char *normalized = malloc(strlen(text) + 1);
    if (normalized == NULL) {
        abort();
    }

    char *dst = normalized;
    for (const char *src = text; *src != '\0'; ++src) {
        *dst++ = *src;
        if (*src == ' ' && src[1] == ' ') {
            ++src;
        }
    }
    *dst = '\0';
    return normalized;
}
