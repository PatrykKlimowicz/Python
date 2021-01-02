# let's say that we want to sort list, but some numbers must come first as they have higher priority
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


# above function will work for simple inputs:
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
high_priority = {2, 3, 5, 7}
sort_priority(numbers, high_priority)
print(numbers)
# This works as expected because:
# 1. Python support closures. Closure is a function that refer to variables from scope in which there where defined. This is why the helper function is able to access the group argument passed to sort_priority

# 2. Functions are first-class objects in Python, which means you can refer to them directly, assign them to variables, pass them as arguments to other functions, compare them in expressions and if statements, and so on. This is how sort method can accept a closure function as the key argument

# 3. Python has specific rules for comparing sequences. It first compares items at index zero; then, if those are equal, it compares items at index one, and so on. This is why the return value from the helper closure causes the sort order to have two distinct groups.


# Let's try to add functionality to tell if given numbers where in higher prioryty group
def sort_priority_1(values, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found


res = sort_priority_1(numbers, high_priority)
print(numbers, res)

# the sort once again works correctly, but result should be True istead of False. Why it didn't work? So, when we try to return the found variable Python does the following to resolve its reference:
# 1. Search in current scope
# 2. Search in any enclosing scopes
# 3. Search in global scope (scope of the module)
# 4. The built-in scope
# So sort_priority_1 did not fully work because Python thinks we define found variable for sort_priority_1 scope and one for helper closure scope. To make this work we need to use nonlocal keyword:


def sort_priority_2(values, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found


res = sort_priority_2(numbers, high_priority)
print(numbers, res)
# Now it works great! But nonlocal keyword should not be used anywhere but simple functions due to possible problems with tracking our variables. For bigger problems we can use simple class:


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(high_priority)
numbers.sort(key=sorter)
assert sorter.found is True  # OK
