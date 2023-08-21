import os 
import sys
import math


class EquationTwo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def calculate_delta(self) -> float:
        # delta = b**2-4ac
        self.delta = float((self._b**2)-4*(self._a)*(self._c))
        return self.delta


    def check_delta(self) -> int:
        """ this method return number of answers """
        if self.delta == 0:
            return 1
        elif self.delta > 0:
            return 2
        else:
            return 0


    def calculate_answer(self):
        # -b - sqrt(delta) / 2a
        # -b + sqrt(delta) / 2a

        return [ ((-(self._b) - math.sqrt(self.delta))/2*self._a), (-(self._b) + math.sqrt(self.delta))/2*self._a ]


    @property
    def a(self):
        return a


    @a.setter
    def set_a(self, value):
        if not(value != 0):
            print("IMPOSSIBLE")
            sys.exit(1)
        self._a = value



    @property
    def b(self):
        return b



    @b.setter
    def set_b(self, value):
        if not(value != 0):
            print("IMPOSSIBLE")
            sys.exit(1)
        self._b = value

        
    @property
    def c(self):
        return c

    @a.setter
    def set_a_value(self, value):
        if not (a != 0):
            raise ValueError("IMPOSIBLE a cannot be 0")



def main():
    EquationTwo(a=0, b=0, c=0)


if __name__ == "__main__":
    main()