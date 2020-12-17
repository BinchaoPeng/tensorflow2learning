import tensorflow as tf
from sklearn import datasets
import numpy as np

batch_size = 32
epoch = 200

"""
divide train set and test set 
"""
x_train = datasets.load_iris().data
y_train = datasets.load_iris().target

# shuffle
np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)

# cast
x_train = tf.cast(x_train, dtype=tf.float32)
y_train = tf.cast(y_train, dtype=tf.float32)

model = tf.keras.models.Sequential(
    [
     tf.keras.layers.Dense(10, activation="relu",
                           kernel_regularizer=tf.keras.regularizers.l2()),
     tf.keras.layers.Dense(3, activation="relu",
                           kernel_regularizer=tf.keras.regularizers.l2())
     ]
)

model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=["sparse_categorical_accuracy"])

model.fit(x_train, y_train,
          batch_size=batch_size, epochs=epoch,
          validation_split=0.2, validation_freq=10)

model.summary()
