# Day 23 - Enforce clarity with keyword-only and positional-only arguments

---

Please check the day23.py to know to the topic from the code perspective.

## Things to remember:

-   Keyword-only arguments force callers to supply certain arguments by keyword, which makes the intention of a function call clearer.
-   Positional-only arguments ensure that callers can't supply certain parameters using keywords, which helps reduce coupling. Positional-only arguments are defined before single / in the argument list.
-   Parameters between the / and and \* characters in the argument list may be supplied by position or keword, which is the default for Python parameters.
