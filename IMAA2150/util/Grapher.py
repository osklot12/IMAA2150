import numpy as np
import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, title="Graph", x_label="x", y_label="y", grid=True, color="blue", scatter_color="red"):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.grid = grid
        self.color = color
        self.scatter_color = scatter_color


    def _configure_graph(self):
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        if self.grid:
            plt.grid(True)


    def graph_cubic_spline(self, spline_coef, knots, res=100):
        a, b, c, d = spline_coef
        x_vals = [knot[0] for knot in knots]
        n = len(x_vals)

        x_plot = []
        y_plot = []

        h = 1 / res
        for i in range(n - 1):
            x_i = x_vals[i]
            while x_i < x_vals[i + 1]:
                x_plot.append(x_i)
                y_plot.append(
                    a[i] + b[i] * (x_i - x_vals[i]) + c[i] * (x_i - x_vals[i])**2 + d[i] * (x_i - x_vals[i])**3
                )
                x_i += h



        plt.plot(x_plot, y_plot, color=self.color, label="Cubic Spline")

        knot_x = [knot[0] for knot in knots]
        knot_y = [knot[1] for knot in knots]
        plt.scatter(knot_x, knot_y, color=self.scatter_color, label="Knots")

        self._configure_graph()
        plt.legend()
        plt.show()