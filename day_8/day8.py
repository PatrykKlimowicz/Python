# assignment expressions is also called walrus operator. It is useful as it allows to assign variables in places where simple assignment operator is forbiden.

# fruits we have in our shop
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


# simulate lemonade making
def make_lemonade(count):
    print("Making lemonade...")
    return 'lemonade'


# simulate out of stock situation
def out_of_stocks():
    print("Out of stocks!")


# withour walrus operator we'll do something like this:

# we need at least one lemon to make lemonade for customer
count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stocks()

# this code seems ok, but there are some problems:
# count variable is using only in first block, but it is available it else-block as well. This is not important variable, however defining it above if-statement makes it seems special. We can improve readability of this code and its purpose with walrus operator

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stocks()

# Now the code is a lot more readable. This is clear that count variable is suppose to be used only in first block and that else-block is independent of that variable.


# let's say that for cider we need 4 apples as they are not as juicy as lemons. It's possible to use walrus operator in this case as well. But first we'll see how it looks without it.
def make_cider(count):
    print("Making cider...")
    return 'cider'


count = fresh_fruit.get('apple', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stocks()

# and now with walrus operator:
if (count := fresh_fruit.get('apple', 0) >= 4):
    make_cider(count)
else:
    out_of_stocks()

# parentheses are necessary because assignment expression is subexpression


# walrus operator is usefull when we need to assign a variable in the enclosing scope depending on some condition, and then reference that variable shrotly afterward in a function call.
# Let's say we want to make smoothies. To make one we need at least 2 bananas worth of slices, or else OutOfBananas exception will be raised.
def slice_bananas(count):
    print("Slicing bananas.")
    return count * 8


class OutOfBananas(Exception):
    pass


def make_smoothies(count):
    print("Making smoothie")
    if not count:
        raise OutOfBananas
    else:
        return 'smoothie'


# first without walrus operator to better see the differnce later
pieces = 0
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothie = make_smoothies(pieces)
    print("I have", smoothie)
except OutOfBananas:
    out_of_stocks()

# another approach
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothie = make_smoothies(pieces)
    print("I have", smoothie)
except OutOfBananas:
    out_of_stocks()

# And now let's see how walrus operator will improve the code
pieces = 0
if (count := fresh_fruit.get('banana', 0) >= 2):
    pieces = slice_bananas(count)

try:
    smoothie = make_smoothies(pieces)
    print("I have a walrus", smoothie)
except OutOfBananas:
    out_of_stocks()


# walrus operator is also helpful to simulate switch/case statement. Common approach is deeply nested if/elif/else statements:
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('lemon', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = 'Nothing'

# end now same code with walrus operator
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif (count := fresh_fruit.get('lemon', 0)):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

# now the code is clean and readable


# walrus operator can also simulate do/while loops:
def pick_fruit(fruit):
    fresh_fruit[fruit] -= 1
    res = {fruit: fresh_fruit.get(fruit, 0)}
    return res if res[fruit] else None


def make_juice(fruit, count):
    print("Making juice")
    return f'{fruit} juice'


# make fruits as long as there are fruits
bottles = []
while fresh_fruits := pick_fruit('apple'):
    for fruit, count in fresh_fruits.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
