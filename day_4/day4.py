# Python has a built in immutable, ordered sequence type called tuple. Tuple in simplest case is a pair of values simillar to key-vaule pair in dictionary.

# declare a dictionary:
snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}

# use snack_calories to create a tuple of tuples:
items = tuple(snack_calories.items())
print(items)  # ((chips, 140), (popcorn, 80), (nuts, 190))

# immutable means You cannot change its elements
try:
    items[0][0] = 'Big Candy'
except TypeError:
    print('Tuple is immutable!!')

# tuple's elements can be accessed via indexing:
t = ('Jelly', 'Chocolate')
first = t[0]
second = t[1]
print(first, 'and', second)

# above example is not nice and can be achieved in a better way. Code will be more elegant and eye-friendly if the unpacking is used.
first, second = t  # unpacking
print(first, 'and', second)

# The same pattern of unpacking works when assigning to lists, sequences, and multiple levels of arbitrary iterables within iterables
favourite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favourite_snacks.items()

print(f'Favourite {type1} is {name1} with {cals1} calories')
print(f'Favourite {type2} is {name2} with {cals2} calories')
print(f'Favourite {type3} is {name3} with {cals3} calories')

# unpacking can be used to swap values


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]  # swap with unpacking


names = ['John', 'David', 'Michael', 'Arturo', 'Amanda']
print('Before sort: ', names)
bubble_sort(names)
print('After sort: ', names)

# swap in bubble sort works as followes:
# 1. Right site is evaluated to unnamed, temporary tuple (a[i], a[a - 1])
# 2. Unpacking is used to assign values to left side
# 3. Temporary tuple is gone

# unpacking is also useful in for loops:
snacks = [('bacon', 350), ('donout', 240), ('muffin', 190)]
for id, (name, cals) in enumerate(snacks, 1):
    print(f'#{id}:  {name} has {cals} calories')

# for list there is one more functionality, but we'll discover it later ;)
