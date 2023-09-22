import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.animation as animation

fig_1 = plt.figure(1, figsize=[5, 5])
square_points = np.array([[-0.04, -0.04],
                                [-0.04, 0.04],
                                [0.04, 0.04],
                                [0.04, -0.04]])

origin = np.array([[0, np.sqrt(3) / 3],
                        [-0.5, -np.sqrt(3) / 6],
                        [0.5, -np.sqrt(3) / 6]])

triangle_points = square_points*10#np.array([[0, 2*(np.sqrt(1**2 - 0.5**2))/3], [-0.5, -(np.sqrt(1**2 - 0.5**2)) / 3], [0.5, -(np.sqrt(1**2 - 0.5**2))/3]])
p = Polygon(triangle_points, closed=False)
p.set_color('r')
grid_1 = fig_1.add_subplot()
grid_1.add_patch(p)
plt.xlabel("x")
plt.ylabel("y")
plt.axis([-5, 5, -5, 5])
plt.grid()
plt.title("Pioneer P3DX - Simulator")


def init():
    return p,


def animate1(i):
    triangle_points[:, 1] += i
    print(triangle_points)
    p.set_xy(triangle_points)
    return p,


ani = animation.FuncAnimation(fig_1, animate1,
                              frames=np.arange(0, 10, 0.0001),
                              init_func=init,
                              interval=10,
                              blit=True)

plt.show()

"""
pts = np.array([[0, 0.866], [-0.5, -0.289], [0.5, -0.289]])
p = Polygon(pts, closed=False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(-7, 7)
ax.set_ylim(-8, 8)
plt.show()
"""