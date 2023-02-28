

words = ['apple', 'banana', 'cherry', 'date']
w2 = words  # alias, not copy
words.append('elderberry')
print(f"words: {words}")
print(f"w2: {w2}")
print()
w3 = words[::]  # new list, not an alias
words.append('fig')
print(f"words: {words}")
print(f"w2: {w2}")
print(f"w3: {w3}")
w4 = words[::-1]
print(f"w4: {w4}")




