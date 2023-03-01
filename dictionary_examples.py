from sqlalchemy.testing import adict

d1 = dict()
d2 = {'red': 5, 'green': 2}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
    'ALB': 'Albany',
}

print(f"airports['RDU']: {airports['RDU']}")

airports['FIR'] = "Florence"
airports['FLL'] = "Fort Lauderdale"

# print(f"airports['MIA']: {airports['MIA']}")
print(f"airports.get('MIA', 'NOT FOUND'): {airports.get('MIA', 'NOT FOUND')}")
print(f"airports.get('MCO', 1234): {airports.get('MCO', 1234)}")
print(f"airports.get('MIA'): {airports.get('MIA')}")

print(f"airports.setdefault('CLT', 'Charlotte'): {airports.setdefault('CLT', 'Charlotte')}")
print(f"airports: {airports}")
print()

for code, name in airports.items():
    print(code, name)
print()
print(f"airports.items(): {airports.items()}")
print()

for code, name in zip(airports.keys(), airports.values()):
    print(code, name.upper())
print()

print(f"airports.keys(): {airports.keys()}\n")



