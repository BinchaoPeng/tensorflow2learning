import tensorflow as tf
import numpy as np

a = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float64)

# convert tensor dtype forcely
a1 = tf.cast(a, dtype=tf.int64)
print(a1)

# get min val of tensor in one dim
min = tf.reduce_min(a)
print(min)

# get max val of tensor in one dim,
# dim 0 : v direction; dim 1 : h direction
max = tf.reduce_max(a, 0)
print(max)

# make variable value trainable
w = tf.Variable(a)
print(w)

# tensor compute: add:+; subtract:-; multiply:x(every element with same position); divide:/;
# tensor compute: square:^; pow:^n,default n=3; sqrt: ^0.5;
#                 matmul: matrix multiply
a = tf.fill([2, 2], 2)
b = tf.ones([2, 2], dtype=tf.int32)
print(a)
print(b)
print(tf.add(a, b))
print(tf.multiply(a, b))
print(tf.pow(a, 5))
print(tf.matmul(a, b))

# get dataset by features and labels with tensor or numpy type
features = tf.constant([1, 23, 45, 6])
labels = tf.constant([1, 0, 1, 1])
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
print(dataset)
for item in dataset:
    print(item)
