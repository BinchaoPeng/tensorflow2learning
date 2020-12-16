import numpy as np
import tensorflow as tf

"""
one-hot encoding
trans data to one-hot
param:
    data
    depth = num of category
    
example:
    labels : 0,1,2
    outputs:
            tf.Tensor(
                    [[0. 1. 0.]
                    [1. 0. 0.]
                    [0. 0. 1.]], shape=(3, 3), dtype=float32)
"""
classes = 3
labels = tf.constant([1, 0, 2])
output = tf.one_hot(labels, classes)

print(output)
