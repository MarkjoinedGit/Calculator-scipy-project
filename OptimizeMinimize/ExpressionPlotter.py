import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from pygame.locals import *
import numpy as np

class ExpressionPlotter:
    def __init__(self, size=(1000, 600)):
        pygame.init()
        self.window = pygame.display.set_mode(size, DOUBLEBUF)
        self.screen = pygame.display.get_surface()

    def plot(self, func, point=None):
        # Check if y variable exists

        print(point)
        if 'y' in func:
            fig = pylab.figure(figsize=[4, 4], dpi=100)
            ax = fig.add_subplot(111, projection='3d')  # Create AxesSubplot
            x = y = pylab.linspace(-10, 10, 100)  # create array of x and y
            X, Y = pylab.meshgrid(x, y)  # create meshgrid (X, Y)

            # Vectorize the function
            func_vectorized = np.vectorize(lambda x, y: eval(func) if x >= 0 else np.nan)

            # calculate Z foreach X and Y (X, Y)
            Z = func_vectorized(X, Y)

            ax.plot_surface(X, Y, Z)  # draw 3D surface

            # Draw the provided point
            if point is not None:
                ax.scatter(*point[0], point[1], color='r')
        else:
            fig = pylab.figure(figsize=[4, 4], dpi=100)
            ax = fig.gca()
            x = pylab.linspace(-10, 10, 100)  # create array of x
            y = eval(func)  # calculate y foreach x
            ax.plot(x, y)  # draw 2D graph

            # Draw the provided point
            if point is not None:
                x = point[0][0]
                y = point[1]
                ax.scatter(x, y, 10,  'r')  #

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        return surf
