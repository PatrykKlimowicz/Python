# Day 22 - Use _None_ and _docstrings_ to specify dynamic default arguments

---

Please check the day22.py to know to the topic from the code perspective.

## Things to remember:

-   A default argument value is evaluated only once: during function definition at module load time. This can cause odd behaviors for dynamic values like {}. []. datetime.now()
-   Use _None_ as the default value for any keyword argument that has a dunamic value. Document the actual default behavior in the function's docstring.
-   Using _None_ to represent keyword argument default values also works correctly with type annotations.
