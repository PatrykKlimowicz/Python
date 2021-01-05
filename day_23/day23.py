# let's write an advanced function for division operation:
def safe_divison(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# use of this is straightforward:
result = safe_divison(1.0, 0, False, True)
print(result)
result = safe_divison(1.0, 10**500, True, False)
print(result)


# Problem with this function is that, it's easy to confuse boolean arguments.
# To improve that we can use keyword arguments:
def safe_divison_1(number, divisor,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Now calling a function is better:
result = safe_divison_1(1.0, 0, ignore_zero_division=True)
print(result)
result = safe_divison_1(1.0, 10**500, ignore_overflow=True)
print(result)


# However, as we know already, keyword arguments like this above can be simple a positional arguments. But we can force callers to use keyword arguments, by definig a function with keyword-only arguments:
def safe_divison_2(number, divisor, *,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Now calling a function without keyword will raise a TypeError, but with keyword everything works as expected.
result = safe_divison_2(1.0, 0, ignore_zero_division=True)
assert result == float('inf')
try:
    safe_divison_2(1.0, 0)
except ZeroDivisionError:
    pass  # Expected


# Now the problem might occur as number and divisor function parameters might be used as both positional and keyword arguments. In second case there is a problem that in one day name of arguments can changed and every call will be broken since then.
def safe_divison_2(number, divisor, /, *,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Now number and divisor are positional-only arguments:
assert safe_divison_2(2, 5) == 0.4  # OK
# safe_divison_2(number=2, divisor=5)  # ERROR!


# We can add another argument that can be either position or keyword argument:
def safe_divison_3(number, divisor, /,
                   ndigits=10, *,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        fraction = number / divisor
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Now we can call safe_divison_3 with ndigits in many different ways, while first two arguments remain positional-only, and the last two remain keyword-only arguments:
result = safe_divison_3(22, 7)
print(result)

result = safe_divison_3(22, 7, 5)
print(result)

result = safe_divison_3(22, 7, ndigits=2)
print(result)
