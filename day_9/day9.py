# the basic form of slicing is somelist[start:end], the range is <start, end)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:', a[3:5])
print('All but ends:', a[1:7])

# when You slice from the beginning avoid using 0
assert a[:5] == a[0:5]

# when You slice from the beginning avoid using len of sequence
assert a[3:] == a[3:len(a)]

# slicing allows negative values as indexes, and out of bounds values
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[2:-1])
print(a[-3:-1])
print(a[:20])  # the whole list 
print(a[-0:])  # the whole list 

# slicig returns new list, which is not referenced to old one
b = a[2:5]
print("b list before change:    ", b)
print("a list before change:    ", a)
b[0] = 99
print("b list after change:    ", b)
print("a list after change:    ", a)

# when slice is used in assignment it replaces the given range and the lengths does not matter
print("a list before:    ", a)
a[2:7] = [99, 24, 14, 34, 45]
print("a list after:    ", a)

# assigning to a slice with no start and end index replaces the 
# entire contents of the list with a copy of what's referenced
c = a
print("c list before change:    ", c)
print("a list before change:    ", a)
a[:] = [1, 2, 3, 4]
assert a is c  # still the same list objects
c[0] = 1234
print("c list after change:    ", c)
print("a list after change:    ", a)
