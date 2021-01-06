# for given list we want to compute the square of each element
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

# we can achieve the same in simpler and better way - list comprehension
squares = [x**2 for x in a]
print(squares)  # same as earlier

# same can be done with map built-in function, but its worse solution:
squares = map(lambda x: x**2, a)

# list comprehension allows us to easily filter elements:
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

# we have to use filter built-in method if we want to use map for this:
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))
print(even_squares)

# disctionaries and sets had their own comprehensions
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
print(even_squares_dict)

threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(threes_cubed_set)

# this is also possible with map and filter, but its really noisy and hard to read, so should be avoided:
even_squares_dict = dict(
    map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, a)))

threes_cubed_set = set(map(lambda x: x**3, filter(lambda x: x % 3 == 0, a)))
print(even_squares_dict)
print(threes_cubed_set)
