from datetime import datetime, date, timedelta
from dateutil.parser import parse

d = date(2022, 11, 13)
print(f"d: {d}")
print(f"d.year: {d.year}")
print(f"d.day: {d.day}")
print(f"d.month: {d.month}")

t = date.today()
print(f"t: {t}")
print(f"t.day: {t.day}")
print()

now = datetime.now()
print(f"now: {now}")

yoko_bd = date(1933, 2, 18)
raw_age = t - yoko_bd
print(f"raw_age: {raw_age}")

years, days = divmod(raw_age.days, 365)
print(f"Yoko is {years} years and {days} days old")


yoko_bd = "February 18, 1933"
d = parse(yoko_bd)
print(f"d: {d}")

d1 = "Aug 3 2011"
d2 = "4/3/2020"
d3 = "25 May 1975"
d4 = "5-1-2023"
print(f"parse(d1): {parse(d1)}")
print(f"parse(d2): {parse(d2)}")
print(f"parse(d3): {parse(d3)}")
print(f"parse(d4): {parse(d4)}")
print(f"parse(d4, dayfirst=True): {parse(d4, dayfirst=True)}")

d5 = "4 am Oct 31 '79"
print(f"parse(d5): {parse(d5)}")
d6 = "4 pm Oct 31 '79"
print(f"parse(d6): {parse(d6)}")
