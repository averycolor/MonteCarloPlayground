from montecarlo import MontecarloPlotter

class Circle(MontecarloPlotter):
    def get_bounding_box(self, params):
        return [-params[2], params[2]] * 2
    
    def check_hit(self, x, y, params):
        return (x - params[0]) ** 2 + (y - params[1]) ** 2 <= params[2] ** 2
    
print(Circle().simulate([0, 0, 1], 30000, visualize=True))