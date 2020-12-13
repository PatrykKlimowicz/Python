# Before we take that first step...

You are about to start your 90 days long Python adventure. Our journey was planned with "Effective Python" by Brett Slatkin. **But first things first!**
If You want to learn Python I am pretty sure that You have a great sense of style inside You and You pay attention to style of Your code as well...

Please read carefully as this intro is crucial in our journey :)

---

## PEP8

PEP8 stands for _Python Enhancement Proposal #8_. This is the style guide for how to format Python code.

Of course You have freedom to choose. You can either follow PEP8 suggestions or not. If You have some doubts about rules let me share this with You:

I am working in team of 24 programmers. During the day I need to read/write code in 10 repos, hundreds and even thousands lines of codes in files - can You see that with Your imagination?

Ok, now think about 24 different code style, different naming conventions, different visual formatting and much more differences. You got it?

Ok, now imagine that You have to fix a bug - Your client report that if You click on button "A" after You refresh the page with filled form for subscribing newsletter Your application freezes. Seems quite simple? I don not think so... In this case You probably need to read code in couple of files, files with completely different code! How much time will You waste to know how to read the code there? And time is money, right? How many frustrated users will abandon Your client service?

I think You see why PEP8 is that important for us developers. **Let's begin!**
Below You can find some basics of PEP8. Please feel free to check more in Python documentation and use pylint as static code analyzer.

### Whitespace

-   Use spaces instead of tabs for code indentation
-   Use four spaces for each level of syntactically significant indenting
-   Lines should contain no more than 79 characters
-   In a file, functions and classes should be separated by two blank lines
-   In a class, methods should be separated by one blank line
-   In a dictionary, put no whitespace between each key and colon, and put a single whitespace before the value of specific key (if it fits in one line)
-   Put exactly one space before and after "=" sign in a variable assignment
-   For type annotations, ensure that there is no whitespace between variable name and the colon, and use a space before the type information

### Naming

-   Functions, variables and attributes should be in lowercase_underscore format
-   Protected instance attributes should be in \_leading_underscore format
-   Private instance attributes should be in \_\_double_leading_underscore format
-   Classes should be in CaptalizeWord format
-   Module-level constants should be in ALL_CAPS format

### Expressions and Statements

-   Use inline negation instead of negation of positive expressions:

```python
if not a is b:  # wrong

if a is not b:  # OK
```

-   Don't check for empty containers or sequences by comparing the length to zero. Assume that the empty values implicitly evaluates to _False_:

```python
if len(my_empty_list) == 0:  # wrong

if not my_empty_list:  # OK
```

-   Check if containers or sequences are not empty like:

```python
if not_empty_list:  # OK
```

-   Avoid single-line _if_ statements, _for_ and _while_ loops, and _except_ compound statements.
-   Prefer surrounding multiline expressions with parentheses over using the \ line continuation character.

### Imports

-   Always put import statements at the top of a file
-   Always use absolute names for modules when importing them, not names relative to the current module's own path
-   If You **must** do relative imports, use explicit syntax

```python
from . import bar
```

-   Imports should be in the following order (alphabetical order preferred):
    1. standard library modules
    2. third-party modules
    3. your own modules

#### Uff.. That was a lot to take in!

Grab a coffee and join me in the **day 1 of the coding challenge!!**

---

# Day 1 - Know the differences between _bytes_ and _str_

In Python, there are two types that represents sequences of character data:

1. bytes
2. str

Please check the day1.py to know to the topic from the code perspective.

### Things to remember:

1. _bytes_ contains sequences of 8-bit values, and _str_ contains sequences of Unicode code points
2. Use helper functions to ensure that the inputs You operate on are the type of character sequence that You expect.
3. _bytes_ and _str_ instances cannot be used together with operators like +, -, >, < etc.
4. If You want to read or write binary data from/to a file, always open the file in binary mode: _'rb'_ or _'wb'_
5. If You want to read or write Unicode data from/to a file, be careful about your system's default text encoding. Explicitly pass the _encoding_ parameter to _open_ if You want to avoid surprises.
