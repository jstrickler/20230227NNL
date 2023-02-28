list1 = list()
print(f"list1: {list1}")
print(f"len(list1): {len(list1)}")
list2 = ['apple', 'banana', 'peach']
list3 = [5, 9, 8, 14]
list4 = []
#  x = list(any_iterable)
animal = "wombat"
a_list = list(animal)
print(f"a_list: {a_list}")

cities = ['Durham', 'Syracuse', 'Akron', 'Anchorage']
print(f"cities: {cities}")
print(f"len(cities): {len(cities)}")
print(cities[0], cities[2])
cities.insert(0, "Albany")
print(f"cities: {cities}")
cities.insert(3, "Schenectady")
print(f"cities: {cities}")
cities.append("Niskayuna")
print(f"cities: {cities}")
cities.append("Homestead")

# numpy   -- large, efficient, n-dimensional numerical arrays

more_cities = ['Saratoga', 'Glenallen', 'McKeesport']
cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
del cities[2]
print(f"cities: {cities}")

# del x; del some_list; del some_list[x];  del ANYTHING
cities.remove('Homestead')
print(f"cities: {cities}")

print(cities.index('Niskayuna'))

c = cities.pop()
print(f"c: {c}")
print(f"cities: {cities}")
c = cities.pop(2)
print(f"c: {c}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(value)   x = LIST.pop()  x = LIST.pop(pos)
print(f"cities[0]: {cities[0]}")
print(f"cities[5]: {cities[5]}")
print(f"cities[6]: {cities[6]}")
print(f"cities[-1]: {cities[-1]}")   #  cities[len(cities)-1]

# slicing
print(f"cities[0:4]: {cities[0:4]}")

# slices:   [start:stop:step]
#  start is INclusive
#  stop is EXclusive
print(f"cities[:4]: {cities[:4]}")
print(f"cities[2:5] {cities[2:5]}")
print(f"cities[-2:]: {cities[-2:]}")
print(f"cities[:]: {cities[:]}")

place = "Albany, NY"
print(f"place[:6]: {place[:6]}")
print(f"place[-2:]: {place[-2:]}")
print(f"cities: {cities}")

#  for VAR ... in ITERABLE:
#     ...
for city in cities:
    # city = next(cities)
    print(city.upper())
print()
print(f"city: {city}")

cities2 = [cities[i] for i in (1, 2, 5)]
print(f"cities2: {cities2}")








