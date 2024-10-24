import numpy as np

DEFAULT_NUM_ITERATIONS = 1000
DEFAULT_TOL = 1e-6

class PowerIteration:
    def __init__(self, A, num_iterations=DEFAULT_NUM_ITERATIONS, tol=DEFAULT_TOL):
        self.A = A
        self.num_iterations = num_iterations
        self.tol = tol



    def run(self):
        n, m = self.A.shape
        assert n == m, "Matrix must be square"
        v = np.random.rand(n)
        v = v / np.linalg.norm(v)

        for i in range(self.num_iterations):
            v_next = np.dot(self.A, v)
            v_next = v_next / np.linalg.norm(v_next)

            if np.linalg.norm(v_next - v) < self.tol:
                break

            v = v_next

        eigenvalue = np.dot(v, np.dot(self.A, v)) / np.dot(v, v)

        return eigenvalue, v