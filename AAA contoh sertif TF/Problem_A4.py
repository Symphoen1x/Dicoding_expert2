# ==========================================================================================================
# PROBLEM A4
#
# Build and train a binary classifier for the IMDB review dataset.
# The classifier should have a final layer with 1 neuron activated by sigmoid.
# Do not use lambda layers in your model.
#
# The dataset used in this problem is originally published in http://ai.stanford.edu/~amaas/data/sentiment/
#
# Desired accuracy and validation_accuracy > 83%
# ===========================================================================================================
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class MyCallbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        thres = .83
        if logs.get('accuracy') is not None and logs.get('accuracy') > thres and logs.get('val_accuracy') > thres:
            print(f"\n\n\nDesireed training Accuracy is {logs.get('accuracy')}, that is greater than {thres}")
            print(f"\nValidation Accuracy is {logs.get('val_accuracy')}, that is greater than {thres}\n\n")
            self.model.stop_training = True


callbacks = MyCallbacks()


def solution_A4():
    imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)

    train_data, test_data = imdb['train'], imdb['test']
    training_sentences = []
    training_labels = []
    testing_sentences = []
    testing_labels = []

    for s, l in train_data:
        training_sentences.append(s.numpy().decode('utf8'))
        training_labels.append(l.numpy())

    for s, l in test_data:
        testing_sentences.append(s.numpy().decode('utf8'))
        testing_labels.append(l.numpy())

    # Tokenize and pad sequences
    vocab_size = 10000
    embedding_dim = 16
    max_length = 120
    trunc_type = 'post'
    oov_tok = "<OOV>"

    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)

    training_sequences = tokenizer.texts_to_sequences(training_sentences)
    training_padded = pad_sequences(training_sequences, maxlen=max_length, truncating=trunc_type)

    testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
    testing_padded = pad_sequences(testing_sequences, maxlen=max_length, truncating=trunc_type)

    # Build the model
    model = tf.keras.Sequential([
      tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
      tf.keras.layers.GlobalAveragePooling1D(),
      tf.keras.layers.Dense(32, activation='relu'),
      tf.keras.layers.Dropout(0.5),
      tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    history = model.fit(
      training_padded,
      np.array(training_labels),
      epochs=30,
      steps_per_epoch=16,
      validation_data=(testing_padded, np.array(testing_labels)),
      validation_steps=None,
      callbacks=[callbacks])

    # val_data = (testing_padded, np.array(testing_labels))

    # res = model.evaluate('What should I  fill this') # Will results an error

    print("history keys: ", history.history.keys())

    print(f"\nhistory per epoch of desired training accuracy: {history.history['accuracy']}\n")
    if 'val_accuracy' in list(history.history.keys()):
        print(f"\nhistory per epoch of validation accuracy: {history.history['val_accuracy']}\n")
    print(f"\n\n\nDesired Training  Accuracy from history.history['accuracy'][-1]: {history.history['accuracy'][-1]}\n")
    # print(f"\nmodel.evaluate output: {res}\n")
    # print(f"\nValidation Accuracy from model.evaluate: {res[1]}\n")
    # if 'val_accuracy' in list(history.history.keys()):
    print(f"\nValidation Accuracy from history.history['val_accuracy'][-1]: {history.history['val_accuracy'][-1]}\n")
    if 'loss' in list(history.history.keys()):
        print(f"\nNot important, desired training loss from history.history['loss'][-1]: {history.history['loss'][-1]}\n")
    if 'val_loss' in list(history.history.keys()):
        print(f"\nNot important, validation loss from history.history['val_loss'][-1]: {history.history['val_loss'][-1]}\n")

    return model


#solution_A4()

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.


if __name__ == '__main__':
    model = solution_A4()
    model.save("model_A4.h5")
