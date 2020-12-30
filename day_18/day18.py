# let's create a function that divides two numbers
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

# The approach with if statement that check the result is quite wrong as it might causes errors. For example, You can exclude all falsy values like 0, '' and so on:
a, b = 0, 3
result = careful_divide(a, b)
if not result:
    print('Invalid inputs')  # this runs but should not!


# Such misinterpretation of a False-equivalent return value is a common mistake in Pyton code when None has special meaning. There are two ways to get rid of such potential errors:

# First, return a tuple: status, result
def careful_divide_1(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = careful_divide_1(3, 1)
if not success:
    print('Invalid inputs')

# the problem is that user can simply ignore first value:
_, result = careful_divide_1(3, 0)
if not result:
    print('Invalid inputs')  # UPS!


# Second, never return the None for special cases
def careful_divide_2(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs!')


x, y = 5, 2
try:
    result = careful_divide_2(x, y)
except ValueError:
    print('Invalid inputs!')
else:
    print(f'Result: {result:.2f}')


# This can be even better with:
def perfect_divide(a: float, b: float) -> float:
    """
        Divides a by b.

        Raises:
            ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs!')

# Now the inputs, outputs and special cases are clear and there is no doubt about this functionality
