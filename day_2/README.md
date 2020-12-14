# Day 2 - Prefer interpolated f-strings over C-style format strings and str.format

---

Please check the day2.py to know to the topic from the code perspective.

## Thing to remember:

-   C-style format strings that use the % operator suffer from a variety of gotchas and verbosity problems
-   Thee str.format method introduces some useful concepts in its formatting specifiers mini language, but it repeats the misstakes of C-style format strings and should be avoided
-   F-strings are a new syntax for formatting values into strings that solves the biggest problems with C-style format strings.
-   F-strings are succint yet powerfull because the allow for arbitrary Python expressions to be directly embedded within format specifiers.
