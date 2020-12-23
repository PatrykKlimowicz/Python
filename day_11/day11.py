car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
try:
    oldest, second_oldest = car_ages_descending
except ValueError:
    print("You must specify more values to unpack Your list!")

# Newcomers to Python may use slicing nd indexing to solve this:
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

# The above code works, but is visually noisy and error prone as well
# To better handle this situation Python gives us catch-all unpacking:
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)
# Now the code is sorter and easy to read! What's more we don't need to worry about sync in indexes, so this is not error prone approach.

# The starred expression can be in any place:
oldest, *others, youngest = car_ages_descending
print(oldest, others, youngest)

# However You have to specify at least one variable next to starred expression:
# try:
#     *others = car_ages_descending
# except SyntaxError:
#     print("Did You specify at least one variable?")

# You also cannot have two starred expressions in one assignment
# try:
#     first, *second, *third, fourth = car_ages_descending
# except SyntaxError:
#     print("Two starred expressions are not allowed")

# But it is possible to use more than one starred expression when You have nested structures:
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC', 'AWF'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova')
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()
print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')


# Starred expression can be used to unpack arbitrary iterators
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')


it = generate_csv()
header, *rows = it
print('CSV Header:', header)
print('Row count:', len(rows))

# here we have len(rows) equal to 0, keep in mind that unpacking with starred expression always creates a list so unpacking an iterator may make You run out of memory and crash Your program.
