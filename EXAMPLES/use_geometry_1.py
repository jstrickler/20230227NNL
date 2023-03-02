import sys
# load <folder-from-sys.path>/EXAMPLES/alpha/mathlib/geometry.py
from EXAMPLES.alpha.mathlib import geometry

#  PYTHONPATH

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
from EXAMPLES.alpha.mathlib.geometry import ANIMAL

print(f"geometry.PI: {geometry.PI}")

# for path in sys.path:
#     print(path)

print(f"geometry.ANIMAL: {geometry.ANIMAL}")
