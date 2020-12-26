# There are three fundamental operations while working with dictionaries: accesing, assigning and deleting key-value elements. Dictionaries are dynamic and it's common that you'll try to access or delete key that does not exist:
counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

# To increment the value for key we need to check if that specific key exist and if it is not, assign zero as started value
key = 'wheat'
if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

# Another way to achieve above:
try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

# And with using the key method
count = counters.get(key, 0)  # 0 is returned if key isn't present
counters[key] = count + 1

# Using distionary with lists:
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'briche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

# Using in expression requires two accesses if the key is present or one access and one assignment if the key is missing. Same with KeyError exception:
key = 'whole grain'
who = 'John'
try:
    name = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)

# and same with get method
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

# but best is to combine get method with assginment expression:
if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

# Dict provides the setdefault method:
names = votes.setdefault(key, [])
names.append(who)

# This works as expected and it's even shorter than get method so why not use this?
# It's because of lower code readability. setdefault method does getting operation while it's called set, so without knowledge of its behaviour before start reading the code You won't fully understand this from the very beginning. What's more setdefault has one gotcha:
# The default value passed to setdefault is assigned directly into the dictionary when the key is missing instead of being copied:
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before', data)
value.append('hello')
print('After', data)
# This means that we need to make sure that we're always constructing a new default value for each key we access with setdefault method.
