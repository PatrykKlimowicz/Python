# Day 24 - Define function decorators with _functools.wraps_

---

Please check the day24.py to know to the topic from the code perspective.

## Things to remember:

-   Decorators in Python are syntax to allow on function to modify another function at runtime.
-   Using decorators can cause strange behaviors in tools that do introspection, such as debuggers.
-   Use the _wraps_ decorator from the _functools_ built-in module when you define your own decorators to avid issues.
