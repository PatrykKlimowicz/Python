# 90 days of code

In response of my willingness to improve my knowledge and quality of code I dare myself to a challenge:

### New important thing in Python everyday for 90 days

If You want to know best practices please stay tuned.
The main goal is of course to learn and to check my self-discipline as well.

Start: 13.12.2020
End:
Based on "Effective Pyton" by Brett Slatkin

---

### Pythonic thinking ---> DONE

0. Discover the PEP8
1. Know the differences between _bytes_ and _str_
2. Prefer interpolated f-strings over C-style format strings and _str.format_
3. Write helper functions instead of complex expressions
4. Prefer multiple assigment unpacking over indexing
5. Prefer _enumerate_ over _range_
6. Use _zip_ to process iterators in parallel
7. Avoid _else_ blocks after _for_ and _while_ loops
8. Prevent repetition with assignment expressions

### Lists and Dictionaries ---> DONE

1. Know how to slice sequences
2. Avoid striding and slicing in single expression
3. Prefer catch-all unpacking over slicing
4. Sort by complex criteria using the _key_ parameter
5. Be cautious when relying on _dict_ insertion ordering
6. Prefer _get_ over _in_ and _KeyError_ to handle missing dictionary keys
7. Prefer _defaultdict_ over _setdefault_ to handle missing items in internal state
8. Know how to construct Key-Dependent default values with _**missing**_

### Functions ---> DONE

1. Never unpack more than three variables when function returns multiple values
2. Prefer raising exceptions to returning None
3. Know how closures interact with variable scope
4. Reduce visual noise with variable positional arguments
5. Provide optional behavior with keyword arguments
6. Use None and docstrings to specify dynamic default arguments
7. Enforce clarity with keyword-only and positional arguments
8. Define function decorators with functools.wraps

### Comprehensions and Generators ---> DONE

1. Use comprehensions instead of _map_ and _filter_
2. Avoid more than two control subexpressions in comprehensions
3. Avoid repeated work in comprehensions by using assignment expressions
4. Consider generator instead of returning list
5. Be defensive when iterating over arguments
6. Consider generator expression for large list comprehensions
7. Compose multiple generator expressions for large list comprehensions
8. Compose multiple generators with yield from
9. Avoid injecting data into generators with send
10. Avoid causing state transitions in generators with throw

### Classes and Interfaces ---> ACTIVE

1. Compose classes instead of nesting many levels of built-in types
2. Accept functions instead of classes for simple interfaces
3. Use _@classmethod_ polymorphism to construct object generically
4. Initialize parent classes with super
5. Consider composing functionality with mix-in classes
6. Prefer public attributes over private ones
7. Inherit from collections.abc for custom container types

### Metacalsses and attributes

t.b.d

### Concurrency and Parallelism

t.b.d

### Robustness and Performance

t.b.d

### Testing and Debugging

t.b.d

### Collaboration

t.b.d
