# Day 18 -

---

Please check the day18.py to know to the topic from the code perspective.

## Things to remember:

-   Functions that return _None_ to indicate special meaning are error prone because _None_ and other values all evaluate to _False_ in conditional expressions
-   Raise exceptions to indicate special situations instead of returning _None_. Expect the calling code to handle exceptions properly when they're documented.
-   Type annotations can be used to make it clear that function will never return the value _None_, even in special situations.
