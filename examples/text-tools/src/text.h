#ifndef TEXT_TOOLS_TEXT_H
#define TEXT_TOOLS_TEXT_H

/* text must be a non-null, NUL-terminated string.
 * Return a newly allocated string; the caller must free it.
 * Abort if allocation fails.
 */
char *collapse_spaces(const char *text);

#endif
