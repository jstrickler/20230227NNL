import re

rx_integer = re.compile(r"\d+")
rx_ssn = re.compile(r"\d{3}-\d{2}-\d{4}")

aa = 10

print(f"rx_ssn: {rx_ssn}")


