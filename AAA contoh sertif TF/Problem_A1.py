# =================================================================================
# PROBLEM A1
#
# Given two arrays, train a neural network model to match the X to the Y.
# Predict the model with new values of X [-2.0, 10.0]
# We provide the model prediction, do not change the code.
#
# The test infrastructure expects a trained model that accepts
# an input shape of [1].
# Do not use lambda layers in your model.
#
# Please be aware that this is a linear model.
# We will test your model with values in a range as defined in the array to make sure your model is linear.
#
# Desired loss (MSE) < 1e-4
# =================================================================================


import numpy as np
import tensorflow as tf
from tensorflow import keras

# import tensorflow
# import pandas
# import scipy
# import numpy
# import pip
# import wheel
# import setuptools
# import pkg_resources
#
# def get_version(package_name):
#     try:
#         version = pkg_resources.get_distribution(package_name).version
#         return version
#     except pkg_resources.DistributionNotFound:
#         return None
#
# print(f"pip version: {pip.__version__}")
# print(f"setuptools version: {setuptools.__version__}")
# print(f"wheel version: {wheel.__version__}")
# print(f"tensorflow version: {tensorflow.__version__}")
# print(f"pandas version: {pandas.__version__}")
# print(f"scipy version: {scipy.__version__}")
# print(f"numpy version: {numpy.__version__}")
# print(f"Pillow version: {get_version('Pillow')}")
# print(f"tensorflow-datasets version: {get_version('tensorflow-datasets')}")

class MyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = {}):
        thres = 1e-04
        if logs.get('mse') is not None and logs.get('mse') < thres:
            print(f"\nThe desired training MSE is {logs.get('mse')}, that is less than {thres}. but, the desired training MAE is {logs.get('mae')}\n\n")
            self.model.stop_training = True
callbacks = MyCallback()
def solution_A1():
    # DO NOT CHANGE THIS CODE
    X = np.array([-4.0, -3.0, -2.0, -1.0, 0.0, 1.0,
                 2.0, 3.0, 4.0, 5.0], dtype=float)
    Y = np.array([5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                 12.0, 13.0, 14.0, ], dtype=float)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=[1])
    ])

    model.compile(optimizer='sgd', loss="mse", metrics=['mse', 'mae'])

    history = model.fit(
        X,
        Y,
        epochs=8000,
        validation_data=None,
        callbacks=[callbacks],
        verbose=1,
    )

    res = model.evaluate(X, Y)
    print(f"\n\nNumber of epochs executed: {len(history.history['loss'])}\n\n")
    print(f"\nHistory keys: {list(history.history.keys())}\n")

    print(f"Model evaluation: {res}")

    for i,v in history.history.items():
        print(f"\nAll [{i}] loss: {v}\n")


    for i,v in history.history.items():
        print(f"\nThe last [{i}] loss: {v[-1]}\n")

    print(f"\nDesired Training MSE from history.history['mse']: {history.history['mse'][-1]}\n")

    print(f"\nDesired Training MAE from history.history['mae']: {history.history['mae'][-1]}\n")
    print(f"\nvalidation MSE from model.evaluate: {res[1]}\n")
    print(f"\nvalidation MAE from model.evaluate: {res[2]}\n")
    if 'val_mse' in list(history.history.keys()):
        print(f"\nValidation MSE from history.history['val_mse']: {history.history['mse'][-1]}\n")
    if 'val_mae' in list(history.history.keys()):
        print(f"\nValidation MAE from history.history['val_mae']: {history.history['mae'][-1]}\n")
    print(model.predict([-2.0, 10.0]))
    return model

# solution_A1()

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.

if __name__ == '__main__':
   # DO NOT CHANGE THIS CODE
   model = solution_A1()
   model.save("model_A1.h5")