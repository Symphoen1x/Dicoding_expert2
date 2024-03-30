# ======================================================================================================
# PROBLEM A3
#
# Build a classifier for the Human or Horse Dataset with Transfer Learning.
# The test will expect it to classify binary classes.
# Note that all the layers in the pre-trained model are non-trainable.
# Do not use lambda layers in your model.
#
# The horse-or-human dataset used in this problem is created by Laurence Moroney (laurencemoroney.com).
# Inception_v3, pre-trained model used in this problem is developed by Google.
#
# Desired accuracy and validation_accuracy > 97%.
# =======================================================================================================


import urllib.request
import zipfile
import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epochs, logs={}):
        thres = .975
        if logs.get('accuracy') is not None and logs.get('accuracy') > thres and logs.get('val_accuracy') > thres:
            print(f"\n\n\nCancelled, desired training accuracy is {logs.get('accuracy')}, that is already greater than {thres}")
            print(f"\nCancelled, validation accuracy is {logs.get('val_accuracy')}, that is already greater than {thres}\n\n")
            self.model.stop_training = True


callbacks = myCallback()


def solution_A3():
    inceptionv3 = 'https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
    urllib.request.urlretrieve(
            inceptionv3, 'inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5')
    local_weights_file = 'inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

    pre_trained_model = InceptionV3(
      input_shape=(150, 150, 3),
      include_top=False,
      weights=None
    )

    # Load the weights
    pre_trained_model.load_weights(local_weights_file)

    for layer in pre_trained_model.layers:
        layer.trainable = False

    last_layer = pre_trained_model.get_layer('mixed7')

    data_url_1 = 'https://github.com/dicodingacademy/assets/releases/download/release-horse-or-human/horse-or-human.zip'
    urllib.request.urlretrieve(data_url_1, 'horse-or-human.zip')
    local_file = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/horse-or-human')
    zip_ref.close()

    data_url_2 = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/validation-horse-or-human.zip'
    urllib.request.urlretrieve(data_url_2, 'validation-horse-or-human.zip')
    local_file = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/validation-horse-or-human')
    zip_ref.close()

    train_dir = 'data/horse-or-human'
    validation_dir = 'data/validation-horse-or-human'

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=5,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')

    train_generator = train_datagen.flow_from_directory(
      train_dir,
      target_size=(150, 150),
      batch_size=20,
      class_mode='binary')

    validation_datagen = ImageDataGenerator(
      rescale=1/255.0
    )
    validation_generator = validation_datagen.flow_from_directory(
      validation_dir,
      target_size=(150, 150),
      batch_size=20,
      class_mode='binary'
    )

    # Additional layers for more complexity
    x = last_layer.output
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dropout(0.4)(x)  # Adjusted dropout rate
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.3)(x)  # Adjusted dropout rate
    x = layers.Dense(128, activation='relu')(x)  # Additional dense layer
    x = layers.Dropout(0.2)(x)  # Adjusted dropout rate
    x = layers.Dense(64, activation='relu')(x)  # Additional dense layer
    x = layers.Dropout(0.1)(x)  # Adjusted dropout rate
    x = layers.Dense(1, activation='sigmoid')(x)

    model = Model(pre_trained_model.input, x)

    model.compile(
      optimizer=RMSprop(lr=0.0001),
      loss='binary_crossentropy',
      metrics=['accuracy']
      )

    history = model.fit(
        train_generator,
        steps_per_epoch=10,
        epochs=10,
        validation_data=validation_generator,  # Use the same generator for validation
        validation_steps=10,
        callbacks=[callbacks]
        )

    res = model.evaluate(validation_generator)

    # Print validation accuracy from history
    print(f"validation_generator: {validation_generator}")
    print(f"type validation_generator: {type(validation_generator)}")
    print("\n\nhistory keys: ", history.history.keys())

    print(f"\nhistory per epoch of desired training accuracy: {history.history['accuracy']}\n")
    if 'val_accuracy' in list(history.history.keys()):
        print(f"\nhistory per epoch of validation accuracy: {history.history['val_accuracy']}\n")
    print(f"\n\n\nDesired Training  Accuracy from history.history['accuracy'][-1]: {history.history['accuracy'][-1]}\n")
    print(f"\nmodel.evaluate output: {res}\n")
    print(f"\nValidation Accuracy from model.evaluate: {res[1]}\n")
    if 'val_accuracy' in list(history.history.keys()):
        print(f"\nValidation Accuracy from history.history['val_accuracy'][-1]: {history.history['val_accuracy'][-1]}\n")
    if 'loss' in list(history.history.keys()):
        print(f"\nNot important, desired training loss from history.history['loss'][-1]: {history.history['loss'][-1]}\n")
    if 'val_loss' in list(history.history.keys()):
        print(f"\nNot important, validation loss from history.history['val_loss'][-1]: {history.history['val_loss'][-1]}\n")

    return model


# solution_A3()

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.


if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_A3()
    model.save("model_A3.h5")
