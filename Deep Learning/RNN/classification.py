import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# RNN: Increasing vs decreasing sequence
def rnn_sequence_classification():
    print("\nMODEL : RNN - Sequence Classification")
    sequences = []
    labels = []
    for i in range(1000):
        start = np.random.uniform(-5, 5)
        step = np.random.uniform(0.2, 1.0)
        increasing = i % 2 == 0
        direction = 1 if increasing else -1
        sequence = start + direction * step * np.arange(6)
        sequences.append(sequence)
        labels.append(1 if increasing else 0)

    x = np.array(sequences, dtype=np.float32).reshape(-1, 6, 1) / 10.0
    y = np.array(labels, dtype=np.float32)
    indices = np.random.permutation(len(x))
    x, y = x[indices], y[indices]
    x_train, x_test = x[:800], x[800:]
    y_train, y_test = y[:800], y[800:]

    model = Sequential([
        Input(shape=(6, 1)),
        SimpleRNN(16, activation="tanh"),
        Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=12, batch_size=32, verbose=0)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    example = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32).reshape(1, 6, 1) / 10.0
    probability = float(model.predict(example, verbose=0)[0][0])
    print("Test accuracy:", round(float(accuracy) * 100, 2), "%")
    print("Sequence [1,2,3,4,5,6] is:", "Increasing" if probability >= 0.5 else "Decreasing")

if __name__ == "__main__":
    rnn_sequence_classification()
