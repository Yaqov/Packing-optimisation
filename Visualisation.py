from matplotlib import patches
import matplotlib.pyplot as plt
import Elipse

class Visualisation:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

    def add_elipse(self, elipse:Elipse):
        patch_ellipse = patches.Ellipse((elipse.get_x(),elipse.get_y()),elipse.get_b()*2, elipse.get_a()*2, elipse.get_alpha())
        patch_ellipse.fill = False
        self.ax.add_patch(patch_ellipse)
    
    def plot(self):
        # recompute the ax.dataLim
        self.ax.relim()
        # update ax.viewLim using the new dataLim
        self.ax.autoscale_view()
        plt.grid()
        plt.show()