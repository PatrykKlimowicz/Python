# Day 16 - Know how to construct key-dependent default values with \_\_\_missing\_\_\_

---

Please check the day16.py to know to the topic from the code perspective.

## Things to remember:

-   The _setdefault_ method of _dict_ is a bad fit when creating the default value has high computional cost or may raise exceptions.
-   The function passed to _defauldict_ must not require any arguments, which makes it impossible to have the default value depend on the key being accessed.
-   You can define your own _dict_ subclass with a _\_\_missing\_\__ method in order to costruct default values that must know which key was being accessed.
