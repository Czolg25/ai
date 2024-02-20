import numpy
import tensorflow

from Plot import Plot
from Solver import Solver
from functions.SimpleEquation import Equation

def f(x):
    return tensorflow.exp(x)


if __name__ == '__main__':
    x = numpy.linspace(0, 1, 10)
    x = tensorflow.constant(x, shape=(10, 1), dtype='float64')

    equation = Equation()
    solver = Solver(0.1,x,equation.f)

    solver.solve(1000)

    y=solver.calculate(x)
    ys = numpy.exp(x)

    plot = Plot([x,x],[y,ys],["AI","Ścisłe"])
    plot.show()

