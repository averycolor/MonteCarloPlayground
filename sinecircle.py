from montecarlo import MontecarloPlotter
from math import sin, cos, tan

class SineCircle(MontecarloPlotter):
    def check_hit(self, x, y, params):
        x0, y0, r = params
        return cos(x - x0) + sin(y - y0) <= tan(r ** 2)
    
    def get_bounding_box(self, params):
        return [-10, 10, -10, 10]

print(SineCircle().simulate([0, 0, 1], 10000))