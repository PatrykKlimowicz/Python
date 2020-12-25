# Day 13 - be cautious when relying on _dict_ insertion ordering

---

Please check the day13.py to know to the topic from the code perspective.

## Things to remember:

-   Since Python 3.7 you can rely on the fact that iterating a _dict_ instance's contents will occur in the same order in which the keys were initially added
-   Python makes it easy to define objects that act like dictionaries but that aren's _dict_ instances. For these types, you can't assume that insertion ordering will be preserved.
-   There are three ways to be careful about dictionary-like classes:
    -   write code that doesn't rely on insertion ordering
    -   explicitly check for the _dict_ type at runtime
    -   require _dict_ values using type annotations and static analysis
