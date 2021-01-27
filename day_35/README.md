# Day 35 - Compose classes instead of nesting many levels of built-in types

---

Please check the day35.py to know to the topic from the code perspective.

## Things to remember:

-   Avoid making dictionaries with values that are dictionaries, long tuples, or complex nestings of others build-in types
-   Use _namedtuple_ for lightweight, immutable data containers before you need the flexibility of a full class
-   Move your bookkeeping code to using multiple classes when your internal state dictionaries get complicated
