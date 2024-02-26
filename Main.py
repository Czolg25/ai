import numpy
import tensorflow

from Plot import Plot
from Solver import Solver
from functions.SimpleEquation import Equation


if __name__ == '__main__':
    startRange = 0
    endRange = 1
    nn = 10

    n = (endRange - startRange) * nn

    x = numpy.linspace(startRange, endRange, nn)
    x = tensorflow.constant(x, shape=(nn, 1), dtype='float64')

    equation = Equation()
    solver = Solver(0.1,x,equation)

    solver.solve(10000)

    solution = solver.calculate(x)
    exact_solution = equation.exact_solution(x)

    plot = Plot([x,x],[solution,exact_solution],["AI","Ścisłe"])
    plot.show()

    error = abs(solution - exact_solution)
    error_plot = Plot([x], [error], ["Error"])
    error_plot.show()

