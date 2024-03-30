# =====================================================================================
# PROBLEM A2
#
# Build a Neural Network Model for Horse or Human Dataset.
# The test will expect it to classify binary classes.
# Your input layer should accept 150x150 with 3 bytes color as the input shape.
# Don't use lambda layers in your model.
#
# The dataset used in this problem is created by Laurence Moroney (laurencemoroney.com).
#
# Desired accuracy and validation_accuracy > 83%
# ======================================================================================


import os  # Added import statement
import urllib.request
import zipfile
import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        thres = .83
        if (logs.get('accuracy') is not None and logs.get('accuracy') > thres and logs.get('val_accuracy') > thres):
            print(f"\n\n\nDesired Training Accuracy is {logs.get('accuracy')}, that is greater than {thres}, cancelled")
            print(f"\nValidation Accuracy is {logs.get('val_accuracy')}, that is greater than {thres}, cancelled\n\n")
            self.model.stop_training = True


callbacks = myCallback()


def solution_A2():
    # Check if 'data/' directory exists, if not, create it
    if not os.path.exists('data/'):
        os.makedirs('data/')

    data_url_1 = 'https://github.com/dicodingacademy/assets/releases/download/release-horse-or-human/horse-or-human.zip'
    urllib.request.urlretrieve(data_url_1, 'horse-or-human.zip')
    local_file = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/horse-or-human')

    data_url_2 = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/validation-horse-or-human.zip'
    urllib.request.urlretrieve(data_url_2, 'validation-horse-or-human.zip')
    local_file = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/validation-horse-or-human')
    zip_ref.close()

    TRAINING_DIR = 'data/horse-or-human'
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=3,
        width_shift_range=0.0,
        height_shift_range=0.0,
        shear_range=0.0,
        zoom_range=0.0,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    train_generator = train_datagen.flow_from_directory(
      TRAINING_DIR,
      target_size=(150, 150),
      batch_size=32,
      class_mode='binary'
    )
    VALIDATION_DIR = 'data/validation-horse-or-human'
    validation_datagen = ImageDataGenerator(
      rescale=1./255
    )
    validation_generator = validation_datagen.flow_from_directory(
      VALIDATION_DIR,
      target_size=(150, 150),
      batch_size=32,
      class_mode='binary'
    )

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(
      optimizer=RMSprop(lr=0.0001),
      loss='binary_crossentropy',
      metrics=['accuracy'])
    # model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    history = model.fit(
      train_generator,
      steps_per_epoch=20,
      epochs=10,
      validation_data=validation_generator,
      validation_steps=None,
      callbacks=[callbacks]
      )

    res = model.evaluate(validation_generator)

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


#solution_A2()

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.


if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_A2()
    model.save("model_A2.h5")
