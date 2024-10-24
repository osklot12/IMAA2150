import numpy as np

from IMAA2150.Bisection import Bisection
from IMAA2150.CubicSplines import CubicSplines
from IMAA2150.PowerIteration import PowerIteration
from IMAA2150.util.Grapher import Grapher

def power_iteration():
    A = np.array([
        [0.58827988827, 0.0656939634707, 0.0447421296984, 0.041413562839],
        [-0.861988671498, 1.38329181958, 0.487586770541, 0.451313012979],
        [-0.997737351282, 0.828658135312, 1.23175149756, 0.522387201895],
        [-0.872710337947, 0.724818531031, 0.493651516971, 1.12430460882]
    ])
    pow_it = PowerIteration(A)
    eigenvalue, eigenvector = pow_it.run()
    print(eigenvalue, eigenvector)


def qubic_splines():
    knots = [
        [1, 2],
        [2, 4],
        [3, -5],
        [4, 0],
        [5, 2],
        [7, -1],
        [8, 6],
        [9, -2]
    ]
    cs = CubicSplines(knots)
    grapher = Grapher()
    grapher.graph_cubic_spline(cs.coef(), knots)


def bisection():
    f = lambda x: np.cos(x)**2 + 6 - x
    tol = 0.5e-10
    a = 6
    b = 7

    bi = Bisection(f)
    print(bi.run_bisection_method(a, b, tol))


def main():
    qubic_splines()


if __name__ == '__main__':
    main()
