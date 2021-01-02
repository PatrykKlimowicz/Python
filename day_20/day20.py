# using the *args (varargs or star args) can raduce a visual noise of the code and also improve the usability of the code. Firstly, code without varargs:
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers', [1, 2, 4, 3])
log('Hello!', [])

# We have to pass the epmty list now. Its cumbersome and noisy. Now using the varargs we can do something like:


def log_1(message, *values):  # now parameter is *values not values
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log_1('My numbers', 1, 2, 4, 3)
log_1('Hello!')  # Much better


# However using varargs may cause problems as passed iterable is always converted to tuple, so if we passed a generator we can run out of memory:
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)  # print all 10 values!


# varargs are best for situations where we know the number of inputs in the argument list. *args has second isue - we cannot add new positional arguments to a function without migrating every caller:
def log_2(sequence, message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'S: {sequence}, M: {message}, V: {values_str}')


log_2(1, 'Favourites', 2, 4, 5, 6, 8)
log_2(2, 'Hello, World!')
log_2('My brothers ages:', 23, 4, 15, 23)  # This is not OK!
# To avoid this kind of problems we should use keyword-only arguments and even type annotations
