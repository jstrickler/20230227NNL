
person = "Matthew McConaughey"
place = "Texas"
result = 23 / 7

print(person)
print(place)
print(result)

print(person, place)
# output  str(person) + ' ' + str(place) + '\n'

print(person, end=', ')
print(place)
print(person, end='/')
print(place, end='/')
print(result)

print(person, place, result, sep='/')
print(person, place, result, sep='XXX')
print(person, place, result, sep='')

# new (bestest)
s= f"{person} is from {place}"
print(s)
print(f"2 + 2 is {2 + 2}")
print(f"result is {result:.2f}")
print('-' * 60)

# old (pre-3.6)
s= "{} is from {}".format(person, place)   # OLD OLD OLD
print(s)
print("2 + 2 is {}".format(2 + 2))
print("result is {:.2f}".format(result))

# very old (Python 2)
s = "%s is from %s" % (person, place)   # DEPRECATED
print(s)

a = "apple"
x = "pomegranate"
b = "fig"
c = "lime"


print(f"{a:10s}:{x:>8.8s}:{b:>10s}:{c:^10s}:")

