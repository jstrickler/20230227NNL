
colors = dict(red=5, green=18, blue=1, pink=0, grey=27, yellow=5)
print(f"colors: {colors}\n")

# no sorting
for color, num in colors.items():
    print(color, num)
print()

# sort by key
for color, num in sorted(colors.items()):  # No special sort needed to sort by key
    print(color, num)
print()

# sort by value
for color, num in sorted(colors.items(), key=lambda e: (e[1], e[0])): # Sorting by value uses second element of nested (key, value) pairs returned by items()
    print(color, num)
print()