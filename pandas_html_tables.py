import pandas as pd

URL = "https://www.tiobe.com/tiobe-index/"
tables = pd.read_html(URL)

print(f"len(tables): {len(tables)}")

for df in tables:
    print(df)
print('-' * 60)

print(tables[0].info())