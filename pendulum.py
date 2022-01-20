import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot()
ax.axis([-1, 1, -1, 1])

def angle_speed(w_speed, l, h, ang, g=9.8):
    return w_speed - (g / l) * h * np.sin(ang)


def get_angle(ang, h, w_speed):
    return ang + h * w_speed


def animate(i,line,x,y):
    # i - это и есть Фреймс
    angle = get_angle(i, h, angle_speed(w_speed, l, h, i))
    x = np.cos(angle) * l
    y = np.sin(angle) * l
    line.set_data([0,x],[0,y])
    return line,

h = 0
l = 1
w_speed = 0
x = 0
y = 0
line, = ax.plot(x,y)
animation = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), fargs=(line, x, y), interval=30, blit=False)
ax.grid()
plt.show()