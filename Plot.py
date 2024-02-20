import matplotlib.pyplot as plot


class Plot:

    def __init__(self, x_array, y_array, lore_array):  # x y array of numpy array , lore is array
        self.x_array = x_array
        self.y_array = y_array
        self.lore_array = lore_array

    def show(self):
        fig, ax = plot.subplots(dpi=100)

        for i in range(len(self.x_array)):
            ax.plot(self.x_array[i], self.y_array[i], label=self.lore_array[i])

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y(x)$')

        plot.legend(loc='best')
        plot.show()
