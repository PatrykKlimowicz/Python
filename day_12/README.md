# Day 12 - sort by complex criteria using the _key_ parameter

---

Please check the day12.py to know to the topic from the code perspective.

## Things to remember:

-   The _sort_ method of the _list_ type can be used to rearrange a list's contents by the natural ordering of built-in types like strings, integers, tuples, and so on.
-   The _sort_ method doesn't work for objects unless the define a natural ordering using special methods, which is uncommon.
-   The _key_ parameter of the sort method can be used to suppl a helper function that returns the value to use for sorting in place of each item form the _list_
-   Returning a _tuple_ from the _key_ function allows you to combine multiple sorting criteria together. The unary minus operator can be used to reverse individual sort orders for types that allow it
-   For _types_ that can't be negated, you can combine many sorting criteria together by calling the _sort_ method multiple times using different _key_ functions and _reverse_ values, in the order of lowest rank _sort_ call to highest rank _sort_ call
