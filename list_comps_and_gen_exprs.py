fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    new_item = f.upper()
    f0.append(new_item)
print(f"f0: {f0}\n")

#  [thing-you-want for thing in iterable if ...]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"f3: {f3}\n")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [round(n / 37, 3) for n in nums]
print(f"n1: {n1}\n")

print(nums * 5, '\n')  # does not broadcast/apply

# numpy and pandas DO apply operations across all elements

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

dobs = [p[-1] for p in people]
print(f"dobs: {dobs}\n")

fruit_gen = (f.upper() for f in fruits)
#  also generator function, generator class
print(f"fruit_gen: {fruit_gen}")
for fruit in fruit_gen:
    print(fruit)