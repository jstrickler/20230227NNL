
person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(f"person: {person}")
print(f"person[0]: {person[0]}")
print(f"type(person): {type(person)}")
print(person[0], person[1])
print()

a = 5,  # 1-element tuple
b = ()  # empty tuple

first_name, last_name, product, dob = person # iterable unpacking
print(first_name, last_name)

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

print(f"type(people): {type(people)}")
print(f"type(people[0]): {type(people[0])}")
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")

for person in people:
    print(person)
print('-' * 60)


# standard Python idiom:
for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(f"{last_name:10s} {product}")
print('-' * 60)
print(f"last_name: {last_name}")

#  collections.namedtuple

lat_lon = [38.3, 76.8]

latitude, longitude = lat_lon

age_in_days = 32838
years, days = divmod(age_in_days, 365)
print(years, days)








