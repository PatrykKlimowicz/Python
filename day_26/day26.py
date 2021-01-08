# comprehensions can have multiple levels of looping. We can for example flat the matrix into one list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

# Using two for loops is readable and simple. Another example may be calculating a square value of each cell in matrix
squared = [[x**2 for x in row] for row in matrix]
print(squared)

# However, if we need to flat many lists then list comprehensions is not good idea:
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[11, 12, 13], [14, 15, 16]],
    [[21, 22, 23], [24, 25, 26]],
    [[31, 32, 33], [34, 35, 36]],
]

flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)

# This is hard to read. In this case the typical approach is same lenght and much more readable:
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)

# Comprehensions support multiple if conditions. Multiple conditions at the same looplevel have an implicit "and" expression. So we can filter a list of numbers to only even values greater than 4:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

assert b == c  # OK

# Comprehensions can be specified at each level of looping after the for subexpression. Let's create a matrix that contains cells from another matrix which are divisible by 3 in rows that sum to 10 or higher:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = [[x for x in row if x % 3 == 0]
              for row in matrix if sum(row) >= 10]
print(new_matrix)

# Although this example seems ok it's not recommended to use this in real-world projects as this can be confusing. If You'll have problem to decide follow the rule of thumb: avoid using more that two control subexpressions in a comprehension. This could be two conditions, two loops or one condition and one loop. I you have more than this You should use normal if and for statements.
