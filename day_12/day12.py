# the list built-in type provides sort method. By default sort will order a list in ascending order.
num = [4, 7, 12, 87, 3]
num.sort()
print(num)  # from smallest to largest

# sort works for nearly all built-in types, but what about objects?


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})\n'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

try:
    tools.sort()
except TypeError:
    print("\nWrong sort call!")

# often there's an attribute an the object that you'd like to use for sorting. To support this usecase the key parameter that's expected to be a function.
print('\nUnsorted:', tools)
tools.sort(key=lambda x: x.name)
print('\nSorted by name:', tools)
tools.sort(key=lambda x: x.weight)
print('\nSorted by weight:', tools)

# You can specify more operations before sort is executed:
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('\nCase sensitive:', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places, '\n')

# sometimes multiple criteria for sort needs to be applied
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

# use tuple for more sorting criteria
power_tools.sort(key=lambda x: (x.weight, x.name))
print(f'\n{power_tools}')

# reverse order
power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(f'\n{power_tools}')

# for numerical values it's possible to mix sorting directions by using the unary minus operator in the key function. Below it's used to sort by weigt descending and by name ascending.
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(f'\n{power_tools}')

# unary minus operator doesn't work with all types. To solve this we can call sort multimple times on the same list to combine different criteria together
power_tools.sort(key=lambda x: x.name)  # name ascending
# print(f'\n{power_tools}')  # uncomment to see what happened step by step
power_tools.sort(key=lambda x: x.weight, reverse=True)  # weight descending
print(f'\n{power_tools}')

# this approach can contains as many criteria as you want, but you must remember that you have to execute them in the opposite sequence of you want the final list to contain. In our example we want to sort by:
# 1. weight descending
# 2. name ascending
# so first we sort by name and then by weight. The multiple calls produce more code so its better to use tuple in key function
