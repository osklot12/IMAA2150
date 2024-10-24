import numpy as np
from scipy.linalg import lu_factor, lu_solve
# cubic spline interpolation
class CubicSplines:
    def __init__(self, knots):
        self.knots = knots


    def coef(self, fourth_property="natural"):
        a = []
        sigma = []
        delta = []

        n = len(self.knots)
        # create a, sigma and delta for each knot
        for i in range(n - 1):
            a.append(self.knots[i][1])
            sigma.append(self.knots[i + 1][0] - self.knots[i][0])
            delta.append(self.knots[i + 1][1] - self.knots[i][1])

        # creating matrix containing the coefficients for each c_i
        A = np.zeros((n, n))
        for i in range(1, n-1):
            A[i, i - 1] = sigma[i - 1]
            A[i, i] = 2 * sigma[i - 1] + 2 * sigma[i]
            A[i, i + 1] = sigma[i]

        # creating the b vector
        b = np.zeros(n)
        for i in range(1, n-1):
            b[i] = 3 * ((delta[i] / sigma[i]) - (delta[i - 1] / sigma[i - 1]))

        # inserting end conditions
        if "natural" == fourth_property:
            A[0, 0] = 1
            A[n - 1, n - 1] = 1

        # solving for the coefficients of c
        lu, piv = lu_factor(A)
        c = lu_solve((lu, piv), b)

        d = []
        b = []
        # computing the d and b coefficients
        for i in range(n - 1):
            d.append((c[i + 1] - c[i]) / (3 * sigma[i]))
            b.append((delta[i] / sigma[i]) - ((sigma[i] / 3) * (2 * c[i] + c[i + 1])))

        return a, b, c, d