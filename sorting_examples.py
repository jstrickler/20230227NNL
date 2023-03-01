fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

def ignore_case(item):
    sort_value = item.lower()
    print(f"Comparing {item} as {sort_value}")
    return sort_value

f2 = sorted(fruits, key=ignore_case)
print(f"f2: {f2}\n")

def wacky(thing):
    return thing[-1], thing[0]

f3 = sorted(fruits, key=wacky)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=str.lower)  # ignore case
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=len)
print(f"f5: {f5}\n")

def custom_sort(thing):
    return len(thing), thing.lower()

f6 = sorted(fruits, key=custom_sort)
print(f"f6: {f6}\n")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = sorted(nums)
print(f"n1: {n1}\n")
n2 = sorted(nums, reverse=True)
print(f"n2: {n2}\n")

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

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[3]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)


for person in sorted(people, key=lambda person: person[3]):
    print(person)


def by_last_first(p):
    return p[1], p[0]

f7 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"f7: {f7}\n")
