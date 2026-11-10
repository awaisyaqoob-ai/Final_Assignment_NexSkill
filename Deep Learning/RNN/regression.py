import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# RNN: Predict the next number
def rnn_next_number():
    print("\nMODEL : RNN - Next Number Prediction")
    sequences = []
    answers = []
    for _ in range(1500):
        start = np.random.uniform(0, 20)
        step = np.random.uniform(0.5, 3.0)
        values = start + step * np.arange(6)
        sequences.append(values[:5])
        answers.append(values[5])

    x = np.array(sequences, dtype=np.float32).reshape(-1, 5, 1) / 40.0
    y = np.array(answers, dtype=np.float32) / 40.0
    x_train, x_test = x[:1200], x[1200:]
    y_train, y_test = y[:1200], y[1200:]

    model = Sequential([
        Input(shape=(5, 1)),
        SimpleRNN(32),
        Dense(16, activation="relu"),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(x_train, y_train, epochs=25, batch_size=32, verbose=0)
    loss, mae = model.evaluate(x_test, y_test, verbose=0)
    example = np.array([2, 4, 6, 8, 10], dtype=np.float32).reshape(1, 5, 1) / 40.0
    prediction = float(model.predict(example, verbose=0)[0][0]) * 40.0
    print("Test MAE:", round(float(mae) * 40.0, 3))
    print("Predicted next number:", round(prediction, 2), "(expected: 12)")

if __name__ == "__main__":
    rnn_next_number()
