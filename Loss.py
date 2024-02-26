class Loss:
    def __init__(self, f, x):
        self.f = f
        self.x = x

    def term_function(self, x):
        return self.f.term_function(x)

    def calculate(self, n):
        return self.f(n, self.x) ** 2
