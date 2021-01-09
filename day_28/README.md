# Day 28 - consider generators instead of returning lists

---

Please check the day28.py to know to the topic from the code perspective.

## Things to remember:

-   Using generators can be clearer than the alternative of having a function return a list of accumulated results
-   The iterator returned by a generator produces the set of vales passed to yield expressions within the generator function's body
-   Generators can produce a sequence of outputs for arbitrary large inputs because their working memory doesn't include all inputs and outputs
