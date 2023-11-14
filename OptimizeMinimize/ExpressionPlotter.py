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
        # Kiểm tra xem hàm có chứa biến 'y' không
        if 'y' in func:
            fig = pylab.figure(figsize=[4, 4], dpi=100)
            ax = fig.add_subplot(111, projection='3d')  # Tạo một đối tượng AxesSubplot 3D
            x = y = pylab.linspace(-10, 10, 100)  # Tạo mảng x và y
            X, Y = pylab.meshgrid(x, y)  # Tạo lưới điểm (X, Y)

            # Vector hóa biểu thức func
            func_vectorized = np.vectorize(lambda x, y: eval(func) if x >= 0 else np.nan)

            # Tính giá trị Z tại mỗi điểm (X, Y)
            Z = func_vectorized(X, Y)

            ax.plot_surface(X, Y, Z)  # Vẽ bề mặt 3D

            # Vẽ điểm nếu được cung cấp
            if point is not None:
                ax.scatter(*point[0], point[1], color='r')  # 'r' nghĩa là màu đỏ
        else:
            fig = pylab.figure(figsize=[4, 4], dpi=100)
            ax = fig.gca()
            x = pylab.linspace(-10, 10, 100)  # Tạo mảng x
            y = eval(func)  # Tính giá trị y tại mỗi x
            ax.plot(x, y)  # Vẽ đồ thị 2D

            # Vẽ điểm nếu được cung cấp
            if point is not None:
                ax.plot(*point, 'ro')  # 'ro' nghĩa là vẽ một điểm màu đỏ

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        return surf
