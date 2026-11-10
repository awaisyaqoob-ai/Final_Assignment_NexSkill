

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# ANN: Handwritten digit classification
def ann_digits():
    print("\nMODEL : ANN - Digit Classification")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train[:10000].astype("float32") / 255.0
    y_train = y_train[:10000]
    x_test = x_test[:2000].astype("float32") / 255.0
    y_test = y_test[:2000]

    model = Sequential([
        Input(shape=(28, 28)),
        Flatten(),
        Dense(64, activation="relu"),
        Dense(10, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=0)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    prediction = model.predict(x_test[:1], verbose=0)
    print("Test accuracy:", round(float(accuracy) * 100, 2), "%")
    print("Predicted digit:", int(np.argmax(prediction[0])), "Actual:", int(y_test[0]))

if __name__ == "__main__":
    ann_digits()
