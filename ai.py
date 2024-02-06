import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def solution(x):
    return np.exp(x) - x - 1

# Definicja sieci neuronowej
class DiffEqnModel(tf.keras.Model):
    def __init__(self):
        super(DiffEqnModel, self).__init__()
        #self.dense1 = tf.keras.layers.Dense(32, activation='exponential')
        self.dense1 = tf.keras.layers.Dense(32, activation='exponential')
        self.dense2 = tf.keras.layers.Dense(1 , activation='linear')

    def call(self, x):
        x = self.dense1(x)
        x = self.dense2(x)
        return x

# Definicja funkcji treningowej
@tf.function
def train_step(inputs, labels):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = loss_object(labels, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

if __name__ == '__main__':
    a = 1
    b = 2
    m = 1000
    n = (b - a) * m

    # Tworzenie danych treningowych
    x_train = np.linspace(a, b, n)[:, None]  # Punkty x równo rozłożone w przedziale
    y_train =  solution(x_train) # Rozwiązanie dokładne równania y(x) = exp(x) - x - 1

    # Inicjalizacja modelu
    model = DiffEqnModel()

    # Definicja funkcji straty i optymalizatora
    loss_object = tf.keras.losses.MeanSquaredError()
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

    # Proces uczenia
    #epochs = 500000
    epochs = 50000
    for epoch in range(epochs):
        loss = train_step(x_train, y_train)
        if epoch % (epochs/10) == 0:
            print(f"Epoch {epoch}: Loss = {loss.numpy()}")

    # Wizualizacja wyników
    x_test = np.linspace(a+1.5*m*abs(b-a)/n, b, n)[:, None]
    y_pred = model(x_test)
    y_plt = solution(x_test)

    plt.plot(x_test, y_pred, label='Approximated solution')
    plt.plot(x_test, y_plt, 'r--', label='Exact solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Approximation of the Differential Equation Solution')
    plt.legend()
    plt.show()

    y = abs((y_pred - y_plt) * 100 / y_plt)
    plt.plot(x_test, y, label='Błąd w %')
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.title('Funkcja błędu')
    plt.legend()
    plt.show()



