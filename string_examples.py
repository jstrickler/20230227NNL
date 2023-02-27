s1 = "spam\n"   # \n \t \f \b \r
print(s1)
print(len(s1))
s2 = 'spam\n'
print(s2, len(s2))
print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
s3 = """spam\n"""
s4 = '''spam\n'''

print("""Guido's the ex-"BDFL" of Python""")

query = """
select first_name, last_name
from students
where gpa > 92
"""

print(query)

s5 = r"spam\n"
print(s5)