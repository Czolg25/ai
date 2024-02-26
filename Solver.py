import tensorflow

import Loss

class Solver:
    def __init__(self,learning_rate,x,equation):
        self.x = x
        self.equation = equation
        self.loss = Loss.Loss(equation.f,x)

        self.n = tensorflow.keras.Sequential([tensorflow.keras.layers.Dense(units=32, activation='exponential', dtype='float64'),
                         tensorflow.keras.layers.Dense(units=1, activation='linear', dtype='float64')])
        self.optimizer = tensorflow.keras.optimizers.Adam(learning_rate=learning_rate)

    def solve(self,epochs):
        self.n(self.x)

        for i in range(epochs):
            step_count = self.optimizer.minimize(self.__loss__, self.n.trainable_variables)

            if i % (epochs / 10) == 0:
                p = i * 100 / epochs
                print(f"nr kroku {i} / {epochs} {p}% strata = {self.__loss__().numpy()}")

    def calculate(self,x):
        return x*self.n(x)+self.equation.term_function(x)

    def __loss__(self):
        return tensorflow.reduce_mean(self.loss.calculate(self.calculate))
