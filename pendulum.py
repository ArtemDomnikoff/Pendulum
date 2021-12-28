import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def angle_speed(w_speed, l, h, ang, g=9.8):
    return w_speed - (g / l) * h * np.sin(ang)


def angle(ang, h, w_speed):
    return ang + h * w_speed


def animate(line, x, y):
    line.set_ydata(x,y)
    return [line]


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
phasa = np.arange(0, np.pi, 0.1)
x = np.linspace(np.pi/2, -np.pi/2, 100)

line, = ax.plot(np.sin(x), np.cos(x))
'''animation = FuncAnimation(fig, func=animate, frames=60,  fargs=(line, x), interval=30, blit=True, repeat=True)'''
ax.grid()
plt.show()
animation.save('pendulum.gif', writer='imagemagick')