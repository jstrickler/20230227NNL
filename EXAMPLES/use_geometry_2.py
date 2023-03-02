from EXAMPLES.alpha.mathlib import geometry as g
from EXAMPLES.alpha.mathlib.geometry import circle_area
import EXAMPLES.alpha.dbutil

import EXAMPLES.alpha
print(f"EXAMPLES.alpha.MAX_TRIES: {EXAMPLES.alpha.MAX_TRIES}")


a1 = g.circle_area(8)
a2 = g.rectangle_area(10, 12)
a3 = g.square_area(7.9)
print(a1, a2, a3)
