# Day 32 - Avoid injecting data into generators with _send_

---

Please check the day32.py to know to the topic from the code perspective.

## Things to remember:

-   The send method can be used to inject data into a generator by giving the yield expression a value that can be assigned to a variable.
-   Using send with yield from expressions may cause surprising behavior, such as None values appearing at unexpected times in the generator output
-   Providing an input iterator to a set of composed generators is a better approach than using the send method, which should be avoided.
