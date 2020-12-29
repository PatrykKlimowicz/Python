# Day 17 - Never unpack more than three variables when function returns multiple values

---

Please check the day17.py to know to the topic from the code perspective.

## Things to remember:

-   You can have functions return multiple values by putting them in a _tuple_ and having the caller take advantage of Python's unpacking syntax.
-   Multiple return values from a function can also be unpacked by catch-all starred expression.
-   Unpacking in four or more variable is error prone and should be avoided; instead return a small class or _namedtuple_ instance
