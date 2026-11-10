import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, SimpleRNN

np.random.seed(42)
tf.random.set_seed(42)

# CNN: Clothing image classification
def cnn_clothes():
    print("\nMODEL : CNN - Clothing Classification")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = x_train[:10000].astype("float32") / 255.0
    y_train = y_train[:10000]
    x_test = x_test[:2000].astype("float32") / 255.0
    y_test = y_test[:2000]
    x_train = x_train[..., np.newaxis]
    x_test = x_test[..., np.newaxis]
    names = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Boot"]

    model = Sequential([
        Input(shape=(28, 28, 1)),
        Conv2D(16, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(32, activation="relu"),
        Dense(10, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=0)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    prediction = model.predict(x_test[:1], verbose=0)
    print("Test accuracy:", round(float(accuracy) * 100, 2), "%")
    print("Predicted clothing:", names[int(np.argmax(prediction[0]))], "Actual:", names[int(y_test[0])])

if __name__ == "__main__":
    cnn_clothes()
