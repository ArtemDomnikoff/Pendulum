import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def angle_speed(w_speed, l, h, ang, g=9.8):
    return w_speed - (g / l) * h * np.sin(ang)


def get_angle(ang, h, w_speed):
    return ang + h * w_speed


def animate_line(line, x, y):
    line.set_data(x, y)
    return [line]


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ang = np.pi / 2
w_speed = 0
l = 1
h = np.arange(0, np.pi, 0.01)
angl = get_angle(ang, h, angle_speed(w_speed, l, h, ang))
x = np.cos(angl) * l
y = np.sin(angl) * l
line, = plt.plot(x, y)
'''animation = FuncAnimation(fig, func=animate, frames=60,  fargs=(line, x), interval=30, blit=True, repeat=True)'''
ax.grid()
plt.show()
animation.save('pendulum.gif', writer='imagemagick')