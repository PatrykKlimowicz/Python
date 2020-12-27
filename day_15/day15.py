from collections import defaultdict  # needed from line 40


# For dictionaries that we didn't create the best method to handle missing keys is get method, as we saw in day 14th. However, in some cases setdefault is the shortest solution. For example:

# cities we've visited in countries
visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

# to add new cities to the sets whether the country name is already present in the dict or not we can use get method:
if (japan := visits.get('Japan', None)) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')
print(visits)

# with setdefault it is shorter:
visits.setdefault('France', set()).add('Arles')
print(visits)


# but let's say we know how the dictionary is created:
class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)


# The above implementation is not ideal. The setdefault has still its confusing name. The implementation is not efficient as it creates new set instance on evry call (no matter if the given country already exist or not). The defaultdict is what we need here. defaultdict automatically store a default values when a key does not exist. All we need to do is provide a dunction that will return the default value to use if key is missing.
class DefaultVisits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = DefaultVisits()
visits.add('England', 'London')
visits.add('Poland', 'Warsaw')
visits.add('Poland', 'Gryfino')
print(visits.data)
# Now the implementation is clear and we don't have unnecessary empty set creation. But, there are still much more ways to handle this kind of problems. We'll discover them in the future...
