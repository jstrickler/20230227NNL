
actor = "Chris Hemsworth"
print(len(actor), type(actor))
print(actor.upper())   # object.method()
print(actor)
x = actor.upper()

# print(dir(actor))
# print()
# help(str)
print(actor.count('h'))
print(actor.lower().count('h'))
print(actor.removesuffix("worth"))
print(actor.removeprefix("Chris "))
print(actor.removeprefix("Liam "))
words = actor.split()
print(words)
data = "spam:ham:eggs"
words = data.split(':')
print(words)
print(actor.startswith('Chris'))
print(actor.endswith('Liam'))

s = "       All my exes live in Texas       "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

s = "xxxyyyxxxxxxxxxxxxxyAll my exes live in Texasyyyyyyyyyyy"
print(s + "|")
print(s.lstrip("xy") + "|")
print(s.rstrip("xy") + "|")
print(s.strip("xy") + "|")
print()

print(s.replace(' ', '').replace('x', 'M').replace('y',''))
print(actor.replace('Chris', 'Liam'))
print(actor)
print(actor.find("Chris"))
print(actor.find("Liam"))
print(actor.find("worth"))




