import tensorflow


class Diff:
    def calculate(self,f, x):
        with tensorflow.GradientTape() as gradient:
            gradient.watch(x)
            prepare_function = f(x)
        diff = gradient.gradient(prepare_function, x)
        return diff
