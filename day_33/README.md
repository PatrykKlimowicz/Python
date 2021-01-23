# Day 33 - Avoid causing state transitions in generators with _throw_

---

Please check the day33.py to know to the topic from the code perspective.

## Things to remember:

-   The _throw_ method can be used to re-raise exceptions within generators at the position of the most recently executed yield expression.
-   Using _throw_ harms readability because it requires additional nesting and boilerplate in order to raise and catch exceptions.
-   A better way to provide exceptional behavior in generators is to use a class that implements the \_\_iter\_\_ method along with methods to cause exceptional state transitions
