# There is a problem with list comprehensions - it creates new list containing one value for each element in input sequence. As for small data it's useful this may cause running out of memory for big inputs:
value = [len(x) for x in open('text.txt')]
print(value)

# To solve this issue, Python provides generator expressions, which are a generalization of list comprehensions and generators:
it = (len(x) for x in open('text.txt'))
print(it)  # generator object
print(next(it))
print(next(it))

# Another powerful outcome of generator expressions is that they can be composed together. So we can use iterator returned by the generator expression abd use it as the input for another generator expression:
roots = ((x, x**0.5) for x in it)
print(next(roots))

# Please remember that you can use iterator only once!
