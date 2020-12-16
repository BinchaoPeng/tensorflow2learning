import tensorflow as tf
import numpy as np

y = tf.constant([1,2,3],dtype=tf.float64)
y_pr = tf.nn.softmax(y)
print(y_pr)