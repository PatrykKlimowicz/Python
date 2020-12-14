# the most common way to foramt string is by using the % operator
a = 0b10011010
b = 0xc4f
print("Binary number is equal %d, ans hex is equal %d." % (a, b))

# the syntax of above code is from C's printf function. %d will be evaluated as # integer number. Despite this style is common there are some problems:

# 1. Changing the order of values in tuple (or format strings on left site) can lead to errors:

val = 1.23
key = "abc"

print("key %-10s val %.2f." % (key, val))  # OK
try:
    # tuple and format strings are mixed
    print("key %-10s val %.2f." % (val, key))
except TypeError:
    print("Error occured")


# 2. C style string are hard to read
pantry = [
    ('avocado', 3.4),
    ('bananas', 2.7),
    ('cherries', 15.3),
]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)))

# 3. To use value multiple times You have to repeat it in tuple:
name = "Patryk"
print("Hi %s! What is Your lastname %s?" % (name, name))

# 4. Using dictionaries in C-style string increases verbosity:
soup = "chicken soup"
print("Today's soup is %(soup)s" % {'soup': soup})

#
#
# interpolated format strings (f-strings)

# f-string allows to use variables from current scope
key = "f_string_key"
value = 100.456
print(f"{key} = {value}")

# output can be formatted
print(f"{key!r:<20s} = {value:.2f}")

# f-trings are more readable. Same example as before:
for i, (item, count) in enumerate(pantry):
    print(f"#{i + 1}: {item.title():<10s} = {round(count)}")

# f-strings can work with python expressions
places = 3
num = 1.123456789
print(f"{num:.{places}f}")
