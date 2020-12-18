# Day 6 - use _zip_ to process iterators in parallel

---

Please check the day4.py to know to the topic from the code perspective.

## Things to remember:

-   The _zip_ built-in function can be used to iterate over multiple iterators in parallel
-   _zip_ creates a lazy generator that produces tuples, so it can be used on infinitely long inputs
-   _zip_ truncates its output silently to the shortest iterator if you supply it with different lengths
-   Use _zip_longest_ from _itertools_ built-in module if you want to use _zip_ on iterators of unequal lengths without truncation
