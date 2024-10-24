import numpy as np
class Bisection:
    def __init__(self, f):
        self.f = f


    def _get_root(self, a, b, tol):
        # check if a root exists by the intermediate value theorem
        if (self.f(a)*self.f(b)) > 0:
            raise ValueError("There exists no root in the given interval.")

        while self.f(self._midpoint(a, b)) > tol:
            c = self._midpoint(a, b)
            print("A:", a, "C:", c, "B:", b)
            if self.f(a)*self.f(c) < 0:
                b = c
            else:
                a = c

        return self._midpoint(a, b)


    def _midpoint(self, a, b):
        return (a + b) / 2


    def run_bisection_method(self, a, b, tol):
        try:
            return self._get_root(a, b, tol)
        except ValueError as e:
            print(e)
