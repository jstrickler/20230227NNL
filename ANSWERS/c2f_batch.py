import sys

for raw_value in sys.argv[1:]:

    celsius = float(raw_value)

    fahrenheit = ((9 * celsius) / 5) + 32

    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

