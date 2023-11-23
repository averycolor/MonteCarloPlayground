from random import uniform
import matplotlib.pyplot as plt

class MontecarloPlotter:
    def check_hit(self, x, y, params):
        return False
    
    def get_bounding_box(self, params):
        return [-1, 1, -1, 1]

    def simulate(self, params, sample_count, visualize = True):
        fig = plt.figure()
        ax = fig.gca()

        hit_count = 0
        box = self.get_bounding_box(params)

        for _ in range(sample_count):
            sample_x = uniform(box[0], box[1])
            sample_y = uniform(box[2], box[3])
            pointColor = "r"

            if self.check_hit(sample_x, sample_y, params):
                pointColor = "g"
                hit_count += 1

            ax.plot(sample_x, sample_y, pointColor + "o")
        
        box_area = abs((box[1] - box[0]) * (box[3] - box[2]))

        if visualize:
            plt.show()

        return box_area * (hit_count / sample_count)