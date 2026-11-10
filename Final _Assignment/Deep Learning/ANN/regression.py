

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# ANN: Number prediction
def ann_regression():
    print("\nMODEL : ANN - Regression")
    x = np.linspace(0, 10, 500, dtype=np.float32).reshape(-1, 1)
    y = 3 * x + 2  # Learn the relationship y = 3x + 2

    model = Sequential([
        Input(shape=(1,)),
        Dense(16, activation="relu"),
        Dense(8, activation="relu"),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(x, y, epochs=30, batch_size=32, verbose=0)
    loss, mae = model.evaluate(x, y, verbose=0)
    prediction = model.predict(np.array([[5.0]], dtype=np.float32), verbose=0)
    print("Mean absolute error:", round(float(mae), 3))
    print("Prediction for x=5:", round(float(prediction[0][0]), 2), "(expected: 17)")

if __name__ == "__main__":
    ann_regression()
