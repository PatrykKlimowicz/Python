# Day 19 - Know how closures interact with variable scope

---

Please check the day19.py to know to the topic from the code perspective.

## Things to remember:

-   Closure functions can refer to variables from any of the scopes in which they were defined.
-   By default, closures can't affect enclosing scopes by assigning variables.
-   Use _nonlocal_ statement to indicate when a closure can modify a variable in its enclosing scopes.
-   Avoid using _nonlocal_ statements for anything beyond simple functions.
