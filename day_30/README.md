# Day 30 - Consider generator expressions for large list comprehensions

---

Please check the day30.py to know to the topic from the code perspective.

## Things to remember:

-   List comprehensions can cause problems for large inputs by using too much memory
-   Generator expressions avoid memory issues by producing outputs one at a time as iterators
-   Generator expressions can be composed by passing the iterator from one generator expression into the for subexpression of another.
-   Generator expressions execute very quickly when chained together and are memory efficient
