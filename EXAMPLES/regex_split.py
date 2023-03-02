import re
from collections import Counter

#    r"\b(?P<first_letter>)[a-z])(?P<guts>[a-z]*)(?P<last_letter)[a-z])\b"

#    r"\*[a-z ]+\*

#   *foo blah bag*

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est dlaborum"""


# pattern is one or more non-letters
rx_wordsep = re.compile(r"[^a-z0-9']+", re.I)  # When splitting, pattern matches what you don't want

words = rx_wordsep.split(s.lower())  # Retrieve text _separated_ by your pattern
unique_words = set(words)

print(sorted(unique_words))
print('-' * 60)
print('-' * 60)

with open('../DATA/alice.txt') as alice_in:
    alice_text = alice_in.read()
    alice_words = rx_wordsep.split(alice_text.lower())
    unique_words = sorted(set(alice_words))
    print(unique_words)
    print("=" * 50)
    alice_word_counter = Counter(alice_words)
    print(alice_word_counter.most_common(100))
    print()
    print(alice_word_counter['gryphon'])
