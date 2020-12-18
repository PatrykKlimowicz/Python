from itertools import zip_longest


# in python we often works with corelated lists
names = ['Patrick', 'David', 'Dominica']
counts = [len(name) for name in names]  # store name lengths in new list

print(counts)

# we need to print longest name
# first approach
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

# second approach -- use enumerate
longest_name = None
max_count = 0
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

# third approach -- use zip to get rid of indexing
longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

# what if we add new name, but not update the counts list?
names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)  # Rosalind is missing

# try to make  Rosalind show as well, now the import from the beginning will be used, -1 is default value for elements that do not have pair
for name, count in zip_longest(names, counts, fillvalue=(-1)):
    print(f'{name}: {count}')
