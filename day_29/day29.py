from collections.abc import Iterator


# common case in python is that we need to iterate over input list multiple time. For example we can count percentage share of each element in sum of this elements:
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


nums = [15, 35, 80]
percentages = normalize(nums)
print(percentages)  # Works great
assert sum(percentages) == 100.0  # OK

# Let's say our app grow and now we need to read input from file. We use generator because in the future we can grow even more:


def read_numbers(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# use it:
it = read_numbers('data.txt')
percentages = normalize(it)
print(percentages)  # []


# This happened because iterator produces its results only a single time. If we iterate over an iterator or generator that has already raised a StopIteration exception, we won't get any results. What is counfused we don't get error that we try to iterate over an empty iterator - for loops, list etc don't bother if there is no output from iterator or if the iterator is exhausted. To solve this we can exhaust (copy) the entire iterator to a list:
def normalize_copy(numbers):
    numbers_copy = list(numbers)  # Copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


# use it:
it = read_numbers('data.txt')
percentages = normalize_copy(it)
print(percentages)  # OK
assert sum(percentages) == 100.0  # OK


# But as we remember from previous days copying the entire iterator to the list can cause running out of memory. We care about scalability of our app so:
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


# to use this function we can pass in a lambda expression that calls the generator and produces a new iterator each time:
path = 'data.txt'
percentages = normalize_func(lambda: read_numbers(path))
print(percentages)  # OK
assert sum(percentages) == 100.0  # OK


# I hope that You find this lambda function clumsy. There is a better way to achieve the same result is to provide a new container class that implements the iterator protocol. The iterator protocol is how Python for loops and related expressions traverse the contents of a container type. When Python sees a statement like "for x in foo" it actually calls iter(foo). The iter built-in function calls the foo.__iter__ special method in turn. The __iter__ method must return an iterator object which implements __next__ method. Then the for loop call this __next__ special method until the iterator is exhausted. So let's define the iterator container that will work for us in that way:
class ReadNumbers:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


numbers = ReadNumbers(path)
percentages = normalize(numbers)
print(percentages)  # OK
assert sum(percentages) == 100.0  # OK


# This work because sum() and for loop will call ReadNumbers.__iter__ independently, whoch will produce two different iterators. Only Downside is that we read data twice. Now we need to specify funciton to ensure that parameters aren't just iterators. The protocol states that when an iterator is passed to the iter built-in function, iter returns the iterator itself. In contrast, when a container type is passed to iter, a new iterator object is returned each time. We can do this in two ways:
# 1:
def normalize_defensive(numbers):
    if iter(numbers) is numbers:  # An iterator --- bad!
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 2: We can use isinstance and collections.abc.Iterator
def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):  # Another way to check
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# So now we can work with lists and container:
nums = [15, 35, 80]
percentages = normalize_defensive(nums)
assert sum(percentages) == 100.0  # OK

numbers = ReadNumbers(path)
percentages = normalize_defensive(numbers)
assert sum(percentages) == 100.0  # OK

it = iter(nums)
normalize_defensive(it)  # ERROR
