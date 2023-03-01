
set1 = {'red', 'blue', 'green', 'purple', 'green'}  # create literal set
set2 = {'green', 'blue', 'yellow', 'orange'}

set1.add('taupe')  # add element to set (ignored if already in set)

print(set1)
print(set2)
print("common:", set1 & set2)  # intersection of two sets
print("all:", set1 | set2)  # union of two sets
print("not common:", set1 ^ set2)  # XOR (symmetric difference); items in one set but not both
print("only set1:", set1 - set2)  # Remove items in right set from left set
print("only set2:", set2 - set1)
print()

food = 'spam ham ham spam spam spam ham spam spam eggs cheese spam'.split()
print(f"food: {food}")

food_set = set(food)  # Create set from iterable (e.g., list)
print(food_set)

with open('../DATA/breakfast.txt') as food_in:
    foods = food_in.read().splitlines()

print(f"foods: {foods}")
print(f"set(foods): {set(foods)}")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

unique_names = set(p[1] for p in people)
print(f"unique_names: {unique_names}")



