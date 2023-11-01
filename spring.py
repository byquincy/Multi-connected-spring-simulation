import math
import time

class Spring:
    def __init__(self, m:float, k:float, offset:float = 0) -> None:
        """
        init
        m: Mass
        k: Spring Constant
        """
        self.m = m
        self.k = k
        self.offset = offset
        self.T = 2*math.pi * math.sqrt(self.m / self.k)
        self.A = 1
    
    def __str__(self) -> str:
        return (
            "[Spring Class]"        + "\n" +
            "m = " + str(self.m)    + "\n" +
            "k = " + str(self.k)    + "\n" +
            "offset = " + str(self.offset)    + "\n" +
            "T = " + str(self.T)    + "\n"
        )
    
    def calcX(self, t):
        return self.
    =A + self.A * math.sin(math.sqrt(self.k / self.m)*t + self.offset)


class Spring2D:
    def __init__(self, s:Spring, radian:float = 0) -> None:
        self.s = s
        self.radian = radian
        self.sin = math.sin(radian)
        self.cos = math.cos(radian)
    
    def __str__(self) -> str:
        return (
            "[Spring 2D Class]"                             + "\n" +
            "> " + str(self.s)                              + "\n" +
            "degree = " + str(math.degrees(self.radian))    + "\n" +
            "sin = " + str(self.sin)                        + "\n" +
            "cos = " + str(self.cos)
        )
    
    def calcCoordinate(self, t) -> tuple:
        """
        calcCoordinate

        return (x, y)
        """
        length = self.s.calcX(t)
        return (length * self.cos, length * self.sin)


BASIS_STAR = 80
if __name__ == "__main__":
    s = Spring2D(Spring(m=2, k=16), 30)
    print(s)

    i = 0
    while True:
        print(s.calcCoordinate(i))
        i += 0.01

    # i = 0
    # while True:
    #     print("\r", end='')
    #     star = BASIS_STAR + int(BASIS_STAR * s.calcX(i))
    #     for j in range(star):
    #         print("*", end='')
    #     for j in range(2*BASIS_STAR - star):
    #         print(" ", end='')

    #     i += 0.01
    #     time.sleep(0.01)