# Day 14 - Prefer _get_ over in and KeyError to handle missing ditionary keys

---

Please check the day14.py to know to the topic from the code perspective.

## Things to remember:

-   There are four comon ways to detect and handle missing keys in dictionaries:
    -   using _in_ expression
    -   KeyError exceptions
    -   the _get_ method
    -   the _setdefault_ method
-   The _get_ method is best for dictionarie that contain basic types like counters, and it is preferable along with assignment expressions when creating dictionary values has high cost or may raise exceptions
-   When the _setdefault_ method of _dict_ seems like the best fit for your problem, you should consider using _defaultdict_ instead.
