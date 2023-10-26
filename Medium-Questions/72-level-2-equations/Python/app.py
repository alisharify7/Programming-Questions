import os
import sys
import math


class EquationTwo:
    def __init__(self):
        self.values = {"a": 0, "b": 0, "c": 0, "delta": 0, "answer": 0}

    def get_a_b_c(self):
        """This Method Get a,b,c for user"""

        def get_float(message: str) -> int:
            """Get Integer Value From user
            Only Int"""
            while True:
                x = input(message)
                try:
                    x = float(x)
                    if x >= -100 and x <= 100:  # −100≤a,b,c≤100
                        return x
                    else:
                        continue
                except ValueError:
                    print("Invalid Value :(\n")
                    continue

        for i in ["a", "b", "c"]:
            self.values[i] = get_float(f"Enter {i}:")

    def calculateDelta(self):
        """
        delta = (b**2)-(4*a*c)
        b^2-4ac
        """
        a, b, c = self.values["a"], self.values["b"], self.values["c"]
        if a != 0 and b != 0:
            self.values["delta"] = (b ** 2) - (4 * a * c)
        else:
            print("IMPOSSIBLE")
            sys.exit(0)

    def print_answer(self):
        a, b, c, delta = self.values["a"], self.values["b"], self.values["c"], self.values["delta"]
        print(f"Delta: {delta}")
        if delta > 0:
            """
            -(b)+(delta)**0.5/2a
            -(b)-(delta)**0.5/2a
            """
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)

            print(f"X1: {round(x1, 3)}")
            print(f"X2: {round(x2, 3)}")
            sys.exit(0)
        elif delta == 0:
            x = -b / (2 * a)
            print(f"X: {round(x, 3)}")
            sys.exit(0)
        else:
            print("IMPOSSIBLE")
            sys.exit(0)


def main():
    e = EquationTwo()
    e.get_a_b_c()
    e.calculateDelta()
    e.print_answer()


if __name__ == "__main__":
    main()
