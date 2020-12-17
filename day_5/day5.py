from random import randint


# range is useful for loops that iterate over a set of integers
random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))

# it is possible to run directly over list elements:
flavour_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavour in flavour_list:
    print(f'{flavour} is delicious')

# often the index of current element is needed
for i in range(len(flavour_list)):
    flavour = flavour_list[i]
    print(f'{i + 1}: {flavour}')

# above example looks complicated despite the fact we only need to print index and element, it looks clumsy as well. We need to use len() function and indexing... Better way is to use enumerate with second param as 1
for idx, flavour in enumerate(flavour_list, 1):
    print(f'{i}:    {flavour}')
