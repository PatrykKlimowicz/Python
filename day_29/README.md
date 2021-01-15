# Day 29 - Be defensive when iterating over arguments

---

Please check the day29.py to know to the topic from the code perspective.

## Things to remember:

-   Beware of functions and methods that iterate over input arguments multiple times. If these arguments are iterators, you may see strange behavior and missing values.
-   Python's iterator protocol defines how containers and iterators interact with the iter and next built-in functions, for loops, and related expressions.
-   You can easily define your own iterable container type by implementing the \_\_iter\_\_ method as a generator.
-   You can detect that a value is an iterator (instead of a container) if calling iter on it products the same value as what you passed in. Alternatively, you can use the _isinstance_ built-in function along with the _collections.abc.Iterator_ class.
