import spring as sp

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

SAMPLING_RATE = 200

class Linker:
    def __init__(self, *springs:sp.Spring2D) -> None:
        self.springs = springs
        self.xBuffer = np.zeros(len(springs) + 1, dtype=float)
        self.yBuffer = np.zeros(len(springs) + 1)
    
    def draw(self, line, t) -> None:
        for i in range(len(self.springs)):
            springCoord = self.springs[i].calcCoordinate(t)
            self.xBuffer[i+1] = self.xBuffer[i] + springCoord[0]
            self.yBuffer[i+1] = self.yBuffer[i] + springCoord[1]
        
        line.set_data(self.xBuffer, self.yBuffer)


fig = plt.figure()
ax = plt.axes(xlim=(-0.5, 3), ylim=(-2, 5))
line, = ax.plot([], [], lw=3)

springs = Linker(
    sp.Spring2D(sp.Spring(m=2, k=16), math.radians(90)),
    sp.Spring2D(sp.Spring(m=2, k=16), math.radians(0)),
    sp.Spring2D(sp.Spring(m=2, k=16), math.radians(-90)),
    sp.Spring2D(sp.Spring(m=2, k=16), math.radians(180)),
)

def animate(i):
    springs.draw(line, i/SAMPLING_RATE)
    # x = s.calcX(i/SAMPLING_RATE)

    # x = np.linspace(-1, x, 100)
    # y = np.zeros(100)
    # line.set_data(x, y)
    return line,

s = sp.Spring(m=2, k=16)
anim = FuncAnimation(fig, animate, frames=int(s.T * SAMPLING_RATE), interval=1000/SAMPLING_RATE)

plt.show()