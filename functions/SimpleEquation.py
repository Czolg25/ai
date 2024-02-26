import numpy

from diffSolver.Diff import Diff

class Equation:

    def __init__(self):
        self.diff = Diff()

    def term_function(self, x):
        return 1

    def f(self,n, x):
        d = self.diff.calculate(n,x)

        return d-n(x)

    def exact_solution(self,x):
        return numpy.exp(x)