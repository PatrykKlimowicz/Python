import pickle  # needed in line 36
from functools import wraps  # needed in line


# Decorator is special Python syntax that can be applied to a function. Decorators run code before and after other function call. They can be use for example to debug function calls.
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

        return result
    return wrapper


# We can apply this decorator to any function with @ symbol:
@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(5)


# there is a problem with presented approach:
print(fibonacci)  # <function trace.<locals>.wrapper at 0x7fb9d40dff70>
# This happened because trace function returns wrapper and this is what after using decerators is assigned to fibonacci, what is executed:
# fibonacci = trace(fibonacci)
# This can be problematic when You have decorators in Your code and the try to debug with tools that do introspection, such as debuggers
# So the help function is useless:
help(fibonacci)  # should be Return the n-th Fibonacci number

# The object serializer breaks as well as it cannot determine the location of the original funtion that was decorated:

# pickle.dumps(fibonacci)  # ERROR


# The solution for above problems is to use wraps helper function from the functools built-in module. This is a decorator that helps to write decorators
def trace_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

        return result
    return wrapper


@trace_2
def fibonacci_2(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


# Everything works as expected now
fibonacci_2(5)
print(fibonacci_2)
help(fibonacci_2)
print(pickle.dumps(fibonacci_2))
