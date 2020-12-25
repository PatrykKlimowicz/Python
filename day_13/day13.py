from collections.abc import MutableMapping  # needed from line 56
from typing import Dict, MutableMapping  # needed from line 116

# In Python 3.5 and before iterating over a dict would return keys in arbitrary order. This means that declaring dictionary in specific order did not means that this order will be a result of print method. Starting with Python 3.6 dictionaries will preserve insertion order.

# Now the order of keyword arguments is always preserved to match how the programmer originally called the function:


def my_func(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} = {v}')


my_func(goose='gosling', kangaroo='joey')


# classes also use the dict type for their instance dictionaries.
class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'


a = MyClass()
for k, v in a.__dict__.items():
    print(f'{k} = {v}')  # order is preserved

# However You shouldn't always assume that insertion ordering behavior will be present when you're handling dictionaries. Python makes it easy to emulate standard protocols matching list, dict and so on. For example, say that we are writing a program to show the results of a contest for cutest baby animal. Here, we start with a dict containing the total vote count for each one:
votes = {
    'otter': 1223,
    'polar bear': 748,
    'fox': 935,
}


# process voting data and save the rank of each animal
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)

    for i, name in enumerate(names, 1):
        ranks[name] = i


# point to the winner of the contest
def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

# the above code works, but imagine that the requirements of this program have changed and now the result should be in alphabetical order insted of rank order


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for k in keys:
            yield k

    def __len__(self):
        return len(self.data)


# the object of SortedDict can be used with functions we declared as this class conforms to the protocol of a standard dictionary:
print()
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

# The result is incorrect because our implementation of get_winner assumes that the dictionary's iteration is in insertion order to match populate_ranks. This asumption is wrong till we use SortedDict instead of dict. There are three ways to mitigate this problem.


# First: reimplement the get_winner function
def conservative_get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name


conservative_winner = conservative_get_winner(sorted_ranks)
print(conservative_winner)  # correct output


# Second: Add explicit check to ensure that ranks is dict type
def check_get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('must provide a dict instance')
    return next(iter(ranks))


check_winner = check_get_winner(sorted_ranks)
# print(check_winner)  # error


# Third use type annotations
# To run this please comment all above lines, uncomment 118-122 and run with
# python3 -m mypy --strict day13.py
# votes = {
#     'otter': 1223,
#     'polar bear': 748,
#     'fox': 935,
# }


def type_populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)

    for i, name in enumerate(names, 1):
        ranks[name] = i


def type_get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class TypeSortedDict(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key: str) -> int:
        return self.data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __iter__(self) -> str:
        keys = list(self.data.keys())
        keys.sort()
        for k in keys:
            yield k

    def __len__(self) -> int:
        return len(self.data)


sorted_ranks = TypeSortedDict()
type_populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = type_get_winner(sorted_ranks)
print(winner)

# after run with "python3 -m mypy --strict day13.py" You'll see that mismatch between the dict and MutableMapping types was found and error is shown. This will prevent mistakes and gotchas.
