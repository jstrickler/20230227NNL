
colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("colors: len is {}; min is {}; max is {}".format(len(colors), min(colors), max(colors)))
print("months: len is {}; min is {}; max is {}".format(len(months), min(months), max(months)))
print()

print("sorted:", end=' ')
for m in sorted(colors):   # sorted() returns a sorted list
    print(m, end=' ')
print()

phrase = ('dog', 'bites', 'man')
rev_phrase = reversed(phrase)
print(f"rev_phrase: {rev_phrase}")

print(" ".join(rev_phrase))  # reversed() returns a reversed iterator
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

print(f"first_names: {first_names}")
print(f"last_names: {last_names}")

full_names = zip(first_names, last_names)  # zip() returns an iterator of tuples created from corresponding elements
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print("{} {}".format(first_name, last_name))




print('-' * 60)
words = ['apple', 'banana', 'cherry', 'date']
for word in words:
    print(word)
print('-' * 60)
rev_words = reversed(words)
print(f"rev_words: {rev_words}")
for word in rev_words:
    print(word)
print('finished')
for word in rev_words:
    print(word)


#  name1 = name2   ==>  creates alias
rev_words = reversed(words)
rw = list(rev_words)
print(f"rw: {rw}")
rw2 = list(reversed(words))
print(f"rw2: {rw2}")


