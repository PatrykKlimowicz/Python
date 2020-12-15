# Python gives opportunity to write a lot of logic in single expression:
from urllib.parse import parse_qs


url_string = "red=5&blue=0&green="
my_values = parse_qs(url_string, keep_blank_values=True)
print(repr(my_values))  # return dict

# try to get some values which could be in url string with get:
print("Red:     ", my_values.get('red'))
print("Green:   ", my_values.get('green'))
print("Opacity: ", my_values.get('opacity'))  # return None

# the None and empty string values are not so nice
# try print 0 for user in such cases with help of boolean expressions

# 'red' key is preset in list returned by get, first param is '5'
# this will implicitly evaluate to True so this is result
red = my_values.get('red', [''])[0] or 0

# get with 'green' key will return list with empty string which implicitly
# evaluates to False so the "or statement" will return the 0
green = my_values.get('green', [''])[0] or 0

# key 'opacity' not exist so the specified default value from get
# (list with empty string is returned). First element - empty string
# will evaluate to false and as a result 0 will be assigned
opacity = my_values.get('opacity', [''])[0] or 0

# check values
print(f"Red:        {red!r}")
print(f"Green:       {green!r}")
print(f"Opacity:     {opacity!r}")

# let's say that we want the results of green, red etc
# as integers so we can use them in math later in the code:
red = int(my_values.get('red', [''])[0] or 0)

# the complexity increases and code is hard to read, so...
red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0

# above is much better, but can improve even more.
# this operation will be repeated multiple times,
# let's us function:


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default


# now code will be much cleaner and user get more freedom to
# easily choose the defaults
green = get_first_int(my_values, green)
print(f"Default green:    {green}")

green = get_first_int(my_values, green, -1)
print(f"Custom default green:    {green}")


# now the code is DRY (don't repeat yourself), more flexible
# and looks nice
