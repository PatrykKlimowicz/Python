import itertools

# In case we need to work with tricky iteration code the itertools might be good help. Some of most common use cases will described here:


############### LINKING ITERATORS TOGETHER ###############
# 1. CHAIN - combine multiple iterators into a single sequential iterator
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

# 2. REPEAT - repeats single value for ever of x times defined by second argument
it = itertools.repeat('hello', 3)
print(list(it))

# 3. CYCLE - repeats an iterator's items forever
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)

# 4. TEE - split single iterator into the number of iterators.
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

# 5. ZIP_LONGEST - join iterators and if they are not equal length return a placeholder
keys = ['one', 'two', 'three']
values = [1, 2]
it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest:', longest)

############### FILTERING ITEMS FROM AN ITERATOR ###############
# 1. ISLICE - slice an iterator by numerical indexes without copying
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print('First five:', list(first_five))
middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds:', list(middle_odds))

# 2. TAKEWHILE - return items from iterator until predicate function returns False for an item
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def less_than_seven(x): return x < 7


it = itertools.takewhile(less_than_seven, values)
print(list(it))

# 3. DROPWHILE - skips items until the predicate function returns True for the first time
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 10]
def less_than_seven(x): return x < 7


it = itertools.dropwhile(less_than_seven, values)
print(list(it))

# 4. FILTERFALSE - return all items from iterator where the predicate function return False
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 10]
def evens(x): return x % 2 == 0


filter_result = filter(evens, values)  # the opposite of filterfalse
print('Filter:', list(filter_result))
filter_false_resutls = itertools.filterfalse(evens, values)
print('Filter false:', list(filter_false_resutls))

############### PRODUCING COMBINATIONS OF ITEMS FROM ITERATORS ###############
# 1. ACCUMULATE - e folds an item from the iterator into a running value by applying a function that takes two parameters. It outputs the current accumulated result for each input value
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 10]
sum_reduce = itertools.accumulate(values)
print('Sum:', list(sum_reduce))


def sum_modulo(first, second):
    output = first + second
    return output % 20


sum_modulo = itertools.accumulate(values, sum_modulo)
print('Sum modulo:', list(sum_modulo))

# 2. PRODUCT - return the cartesian product of items from one or more iterators, which is a nice alternative to using deeply nested list comprehensions
single = itertools.product([1, 2], repeat=2)
print('Single:', list(single))

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))

# 3. PERMUTATIONS - returns the unique ordered permutations of length N with items from an iterator
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

# 4. COMBINATIONS - return the unordered combinations of length N with unrepeated items from an iterator
it = itertools.combinations([1, 2, 3, 4], 3)
print(list(it))

# 5. COMBINATIONS_WITH_REPLACEMENT - same as combinations, but repeated values are allowed
it = itertools.combinations_with_replacement([1, 2, 3, 4], 3)
print(list(it))
