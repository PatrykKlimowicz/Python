import itertools  # needed in line 65

# simplest choice for function that returns a sequence of items is to return a list. For exapmle finding index of every word in a string can be done as:


def index_words(text):
    result = []
    if text:
        result. append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)

    return result


text = 'This is a perfect test text for our function'
result = index_words(text)
print(result)

# There are two problems with index_words function:

# 1. The code is a bit dense and noisy. We call append method each time a new result is found. Quite big part of this function are not needed so it can occupy less space and because of that be more readable

# 2. Fucntion requires all results to be stored in the list before being returned. This can cause troubles for large inputs.

# To solve first (and the second as well) issue is better to use generators. Generators are produced by functions that use yield expressions.:


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

# When called, a generator function does not acctually run but insted immediately returns an iterator. With each call to the next built-in function, the iterator advances the generator to its next yield expression. Each value passed to yield by the generator is returned by the iterator to the caller:


it = index_words_iter(text)
print(next(it))
print(next(it))
print(next(it))

# The index_words_iter is much more simple to read as we remove all interactions with list. The returned iterator can be converted to a list:
result = list(index_words_iter(text))
print(result)


# Second problem: The generator version of our function can be easily adapted to take inputs of arbitrary length due to its bouded memory requirements. We can now create a generator that streams input from a file one line at time and yields outputs one word at a time:
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('text.txt', 'r') as f:
    it = index_file(f)
    # islice will be described in details in future days
    results = itertools.islice(it, 0, 10)
    print(list(results))


# One gotcha about generators like this is that iterator is stateful and cannot be reused.
