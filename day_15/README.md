# Day 15 - Prefer _defaultdict_ over _setdefault_ to handle missing items in iternal state

---

Please check the day15.py to know to the topic from the code perspective.

## Things to remember:

-   If you're creating a dictionary to manage an arbitrary set of potential keys, then You should prefer using a _defauldict_ insatnce from the collections built-in module if it suits your problem
-   If a dictionary of arbitrary keys is passed to you, and you don't control its creation, the you should prefer the _get_ method to access its items. However, it's worth considering using the _setdefault_ method for the few situations in which it leads to shorter code.
