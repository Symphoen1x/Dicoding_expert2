# -*- coding: utf-8 -*-
"""Salinan dari Percobaan project p4.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfO6Wxmxuuju58qP9aBQ2TcdVA8YTIik

##  Import library
"""

#library for pre-processing(cleaning data, transfromation data,  and processing tokenizer)
import pandas as pd
import re,string,unicodedata
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split


#library for model building
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import datetime, os

"""## Preprocessing"""

df = pd.read_csv('new.csv')
df.head(200)

df.info()

nltk.download('stopwords')
nltk.download('punkt')

def clean_text(Text):
    if isinstance(Text, str):
        Text = re.sub(r'http\S+', '', Text)
        Text = re.sub(r'[^a-zA-Z\s]', '', Text)
        Text = Text.lower()
        Text = Text.strip()
        tokens = word_tokenize(Text)
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        Text = ' '.join(tokens)
        return Text
    else:
        return ''

df['cleaned_content'] = df['Tweets'].apply(clean_text)
df.head()

labels = pd.get_dummies(df['Feeling'])
df_baru = pd.concat([df, labels], axis=1)
df_baru = df_baru.drop(columns=['Feeling'])
df_baru.head(20)

tweets = df_baru['cleaned_content'].values
emotion =  df_baru[['angry', 'disgust', 'surprise','sad', 'happy', 'fear']].values
tweets_train, tweets_test, emotion_train, emotion_test = train_test_split(tweets, emotion, test_size=0.2)

# tweets = df_baru['cleaned_content'].values
# emotion =  df_baru[uniq].values
# tweets_train, tweets_test, emotion_train, emotion_test = train_test_split(tweets, emotion, test_size=0.2)

# tokenizer = Tokenizer(num_words=5000, oov_token='x')
# tokenizer.fit_on_texts(tweets_train)
# tokenizer.fit_on_texts(tweets_test)


# sekuens_train = tokenizer.texts_to_sequences(tweets_train)
# sekuens_test = tokenizer.texts_to_sequences(tweets_test)

# padded_train = pad_sequences(sekuens_train,
#                              truncating = 'post',
#                              padding = 'post',
#                              maxlen=maxlen)
# padded_test = pad_sequences(sekuens_test,
#                             truncating = 'post',
#                              padding = 'post',
#                              maxlen=maxlen)

tokenizer = Tokenizer(num_words=5000, oov_token='x')
tokenizer.fit_on_texts(tweets_train)
tokenizer.fit_on_texts(tweets_test)


sekuens_train = tokenizer.texts_to_sequences(tweets_train)
sekuens_test = tokenizer.texts_to_sequences(tweets_test)

padded_train = pad_sequences(sekuens_train,
                             truncating = 'post',
                             padding = 'post',
                            )
padded_test = pad_sequences(sekuens_test,
                            truncating = 'post',
                             padding = 'post',
                             )

"""# Versi pakai transformer"""

class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)

# vocab_size = len(tokenizer.word_index) + 1

# inputs = layers.Input(shape=(None,))
# encoder = layers.Embedding(vocab_size, 16)(inputs)
# transformer_block = TransformerBlock(embed_dim=16, num_heads=2, ff_dim=32)
# encoder = transformer_block(encoder)

# # Tambahkan LSTM di sini
# encoder = layers.LSTM(128)(encoder)

# outputs = layers.Reshape((-1, 128))(encoder)
# encoder = layers.Dropout(0.1)(encoder)
# outputs = layers.GlobalMaxPooling1D()(outputs)
# outputs = layers.Dropout(0.1)(outputs)

# outputs = layers.Dense(128, activation='relu')(outputs)
# outputs = layers.Dropout(0.1)(outputs)
# outputs = layers.Dense(64, activation='relu')(outputs)
# outputs = layers.Dropout(0.1)(outputs)
# outputs = layers.Dense(6, activation='softmax')(outputs)

# model = keras.Model(inputs=inputs, outputs=outputs)

vocab_size = len(tokenizer.word_index) + 1

inputs = layers.Input(shape=(None,))
encoder = layers.Embedding(vocab_size, 16)(inputs)
transformer_block = TransformerBlock(embed_dim=16, num_heads=2, ff_dim=32)
encoder = transformer_block(encoder)

# Tambahkan LSTM di sini
encoder = layers.LSTM(64)(encoder)
encoder = layers.Dropout(0.2)(encoder)

outputs = layers.Reshape((-1, 64))(encoder)
outputs = layers.GlobalMaxPooling1D()(outputs)
outputs = layers.Dropout(0.1)(outputs)

outputs = layers.Dense(64, activation='relu')(outputs)
outputs = layers.Dropout(0.15)(outputs)
outputs = layers.Dense(32, activation='relu')(outputs)
outputs = layers.Dropout(0.15)(outputs)
outputs = layers.Dense(6, activation='softmax')(outputs)

model = keras.Model(inputs=inputs, outputs=outputs)

"""## Model building"""

# model = tf.keras.Sequential([
#     tf.keras.layers.Embedding(input_dim = 5000, output_dim=32),
#     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(128, return_sequences=True, kernel_regularizer=tf.keras.regularizers.l2(0.01), recurrent_regularizer=tf.keras.regularizers.l2(0.01))),
#     tf.keras.layers.GlobalMaxPooling1D(),
#     tf.keras.layers.Dense(512, activation='relu'),
#     tf.keras.layers.Dropout(0.1),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dropout(0.1),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dropout(0,1),
#     tf.keras.layers.Dense(6, activation='softmax'),
#     ])

# model = tf.keras.Sequential([
#     tf.keras.layers.Embedding(input_dim=5000, output_dim=16),
#     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(128, return_sequences=True, kernel_regularizer=tf.keras.regularizers.l2(0.01), recurrent_regularizer=tf.keras.regularizers.l2(0.01))),
#     tf.keras.layers.GlobalMaxPooling1D(),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(64, activation='relu'),
#     # tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(6, activation='softmax')
# ])

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%M%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq = 1)

# custom_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
# model.compile(loss='categorical_crossentropy', optimizer=custom_optimizer, metrics=['accuracy'])
# model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

class AccuracyHistory(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if self.has_reached_accuracy(logs):
            print(' Stop training model, val_accuracy > 90%')
            self.model.stop_training = True

    def has_reached_accuracy(self, logs):
        return (logs.get('accuracy') > 0.90 and  logs.get('val_accuracy') > 0.90)

callbacks = AccuracyHistory()

num_epochs = 30
history = model.fit(padded_train,
                    emotion_train,
                    epochs=num_epochs,
                    validation_data=(padded_test, emotion_test),
                    verbose=2,
                    callbacks=[callbacks, tensorboard_callback])

"""# Melihat plot akurasi training dan testing dengan tensorboard"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs

"""# Melihat plot akurasi training dan testing dengan library matplotlib"""

import matplotlib.pyplot as plt

# Menampilkan grafik loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Menampilkan grafik akurasi
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()