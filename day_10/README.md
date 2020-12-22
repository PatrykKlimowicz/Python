# Day 10 - Avoiding striding and slicing in a single expression

---

Please check the day10.py to know to the topic from the code perspective.

## Things to remember:

-   Specifying start, end and stride in a slice can be extremely confusing
-   Prefer using positive stride values in slices without start or end indexes.
-   Avoid using start, end and stride together in a sigle slice. If you need all three parameters,
    consider doing two assignments or using islice from itertools built-in module
