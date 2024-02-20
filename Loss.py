class Loss:
    def __init__(self, f, x):
        self.f = f
        self.x = x

    def calculate(self, n):
        return self.f(n, self.x) ** 2
