# Python has special syntax for stride of a slice in the form
# somelist[start:end:step]. This let's you get evry nth item from list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = x[::2]  # every second element from the beginning
even = x[1::2]  # every second element from the second element
print(odds)
print(even)

# Striding can be used to reverse a byte string, however it's not obvious at the first sight
z = b'mongoose'
y = z[::-1]
print(y)

# Besides that the negative value for step is not useful and might be confuising
# What will be the results of the following:
print(x[2::2])
print(x[-2::-2])
print(x[-2:2-2])
print(x[2:2:-2])

# Having three numbers within the brackets is hard enough to read because of its density. To avoid this problems split slicing and striding:
a = x[::2]
s = a[1:-1]
print(s)

# In the future wi'll see how to use itertools islice and more ;)
