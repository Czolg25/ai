import numpy

from diffSolver.Diff import Diff

class Equation:

    def __init__(self):
        self.diff = Diff()

    def f(self,n, x):
        d = self.diff.calculate(n,x)
        return d-n(x)