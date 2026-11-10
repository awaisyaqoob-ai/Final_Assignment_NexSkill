

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# CNN regression: predict the numeric value (0 to 9) of a handwritten digit.
# Unlike classification, the last layer outputs one continuous number.
def cnn_regression():
    print("CNN - Digit Value Regression")

    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Convert images from 0-255 to 0-1 and add the channel dimension.
    x_train = x_train[:10000].astype("float32") / 255.0
    x_test = x_test[:2000].astype("float32") / 255.0
    x_train = x_train[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    # Regression targets: numeric values scaled to the 0-1 range.
    y_train = y_train[:10000].astype("float32") / 9.0
    y_test = y_test[:2000].astype("float32") / 9.0

    model = Sequential([
        Input(shape=(28, 28, 1)),
        Conv2D(16, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(32, activation="relu"),
        Dense(1)  # One number, not 10 class probabilities
    ])

    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=1)

    loss, mae = model.evaluate(x_test, y_test, verbose=0)
    predicted = float(model.predict(x_test[:1], verbose=0)[0][0]) * 9.0
    print("Test mean absolute error (digit units):", round(float(mae) * 9, 2))
    print("Predicted numeric value:", round(predicted, 2))
    print("Actual digit:", int(round(float(y_test[0]) * 9)))


if __name__ == "__main__":
    cnn_regression()
