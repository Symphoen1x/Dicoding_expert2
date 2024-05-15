# =============================================================================
# PROBLEM B2
#
# Build a classifier for the Fashion MNIST dataset.
# The test will expect it to classify 10 classes.
# The input shape should be 28x28 monochrome. Do not resize the data.
# Your input layer should accept (28, 28) as the input shape.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 83%
# =============================================================================

import tensorflow as tf

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs is None:
            logs={}
        if (logs.get('accuracy') > 0.96 and logs.get('val_accuracy') > 0.96):
            print("\nAccuracy has achieved, Stop Training!")
            self.model.stop_training=True
def solution_B2():
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (X_train, Y_train), (X_test, Y_test) =fashion_mnist.load_data()
    # NORMALIZE YOUR IMAGE HERE
    X_train, X_test = X_train/255.0, X_test/255.0
    # DEFINE YOUR MODEL HERE
    model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32,(3,3), activation ='relu', input_shape=(28,28,1)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64,(3,3), activation ='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
    ])
    # End with 10 Neuron Dense, activated by softmax
    callback = myCallback()
    # COMPILE MODEL HERE
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    # TRAIN YOUR MODEL HERE
    history = model.fit(
        X_train.reshape(-1, 28, 28, 1),
        Y_train,
        validation_data=(X_test.reshape(-1, 28, 28, 1), Y_test),
        epochs = 500,
        verbose=1,
        callbacks=[callback]
    )


    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_B2()
    model.save("model_B2.h5")
