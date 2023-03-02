import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

rx_code = re.compile(r'(?P<letter>[A-Z])-(?P<number>\d{2,3})', re.I)

s2 = rx_code.sub(r"[\2] {\1} //\g<0>//", s)
print(f"s2: {s2}")
print('-' * 60)
s3 = rx_code.sub(r"\g<number>-\g<letter>", s)
print(f"s3: {s3}")

# backreferences
# \n group n     (not OK to have trailing digits, like \10)
# \g<n> group n  (OK to have trailing digits, like \g<1>0
# \g<spam>  named group "spam"
