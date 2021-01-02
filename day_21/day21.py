# Like in most of other languages in Python you may pass args by position when calling a function:
def reminder(number, divisor):
    return number % divisor


assert reminder(20, 7) == 6

# All normal arguments can be passed by keywords
assert reminder(20, divisor=7) == 6
assert reminder(divisor=7, number=20) == 6

# but keyword params must be after ppositional
# assert reminder(number=20, 7) == 6  # SyntaxError

# each argument can be specified only once
# assert reminder(7, number=20) == 6  # TypeError
# We can use dictionary as input param using the ** operator:
my_numbers = {
    'number': 20,
    'divisor': 7,
}
assert reminder(**my_numbers) == 6

# We can mix both positional and keyword args with ** operator
my_numbers = {
    'divisor': 7,
}
assert reminder(20, **my_numbers) == 6
assert reminder(number=20, **my_numbers) == 6

# We can mix ** operators as long as keys in dictionaries don't overlap
my_number = {
    'number': 20,
}

my_divisor = {
    'divisor': 7,
}
assert reminder(**my_number, **my_divisor) == 6
assert reminder(**my_divisor, **my_number) == 6


# in case we want a function that receives any named keyword arguments we can use **kwargs catch-all parameter
def print_parameters(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} = {v}')


print_parameters(a=1.2, b=5, c=12, d=-7.3)
# Keyword arguments have some benefits:
# 1. Improve code readability: with reminder(number=20, divisor=7) we immediately know which number is number and which is divisor
# 2. Keyword args can have default values specified and because of that code is cleaner and some functionality can be used is special cases while in the same time codu duplication will be avoided
# 3. They provide great way to extend funtionality while providing the backward compability


# So let's say we are reading how much fluid flowing into a vat with some kind of sensor:
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3 kg per secong}')


# in some cases its enough, but sometimes we want to define larger timescales in which sensor will measure the fluid rate
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


flow = flow_rate(weight_diff, time_diff, 1)
print(f'{flow:.3 kg per secong}')


# using default value for parameter is better
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_sec = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print(f'{flow_per_sec:.3 kg per secong}')
print(f'{flow_per_hour:.3 kg per hour}')


# now we want to extend the functionality
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return (weight_diff * units_per_kg / time_diff) * period


flow_per_sec = flow_rate(weight_diff, time_diff)  # works the same
flow_per_hour = flow_rate(weight_diff,
                          time_diff,
                          period=3600)  # works the same

# new functionality
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)

print(f'{flow_per_sec:.3 kg per secong}')
print(f'{flow_per_hour:.3 kg per hour}')
print(f'{pounds_per_hour:.3 pounds per hour}')

# Of course positional arguments can be used in same way as before, but keyword arguments should be used when we work with optional parameters to avoid mistakes
