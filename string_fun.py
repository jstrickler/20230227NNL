name = "john jacob jingleheimer smith"

# put your Python code here:

print(len(name))  # not name.len()
# print(name.__len__())   # not a good practice
print(name.count('j'))  #

print(name.find('jacob'))
print()

pos = -1
while True:
    pos = name.find('j', pos+1)
    if pos == -1:
        break
    print(pos)

import re
positions = [p.start() for p in re.finditer('j', name)]
print(positions)


s = "abcd"
print(s[2])



