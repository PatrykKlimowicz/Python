# Common pattern with comprehensions is the need to reference the same computation in multiple places. For example, we want to manage the orders for a fastener company. As new orders come in from customers, we need to be able to tell them whether we can fulfill their orders. We need to verify that a request is sufficiently in stock and above the minimum threshold for shipping (in batches of 8).
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)

if batches:
    result[name] = batches

print(result)

# Below is same code with dict comprehensions:
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}

# Above code is more compact, but the get_batches call is repeated. It's also visualy noisy error prone as we need to keep in sync two function call. To fix this we can use assignment expression:
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
print(found)

# assignment expression provide the variable that can be used inside comprehension, but the order is important. For example:

# result = {name: (tenth := count // 10)
#           for name, count in stock.items() if tenth > 0}

# The above will raise NameError, because of order the comprehension is evaluated. Fix:
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)
