# the unpacking syntax allows us to return multiple values
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum  # we want to find max and min from list data


lengths = [2, 12, 34, 41, 85, 3, 6, 0]
minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, max: {maximum}')


# use catch-all starred expressions
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:4.0%}')
print(f'Shortest: {shortest:4.0%}')


# our client says that we need to obrain new statistics and return
def new_get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / len

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle + 1]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


minimum, maximum, average, median, count = new_get_stats(lengths)

print(f'Min: {minimum}, max: {maximum}')
print(f'Average: {average}, Median: {median}, Count: {count}')


# The problem of above code is that all returned values are numeric so it's easy to mix them by accident. Second, most likely the line 45 will be too long in real project and needs wrapping so it'll be less readable.
# Situation like this shouldn't happen. You can use three tuples, two variables and one starred expressions. It's better to define lightweight class or namedtuple, but we'll do such thing later.
