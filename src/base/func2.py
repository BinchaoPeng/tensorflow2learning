import tensorflow as tf
import numpy as np

# compute gradient
with tf.GradientTape() as tape:
    a = tf.constant([1, 2, 3], dtype=tf.float64)
    w = tf.Variable(a)
    loss = tf.pow(w, 4)
grad = tape.gradient(loss, w)  # loss是函数，对w求导
print(grad)

# assign_sub  -= after Variable operation
w = tf.Variable(tf.constant([1, 2, 3]))  # must be Variable
w.assign_sub([2, 3, 4])  # w -= [2,3,4]
print(w)

# tf.argmax
# return index of max val in one dim
arr = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
axis0 = tf.argmax(arr, axis=0)  # v direction
axis1 = tf.argmax(arr, axis=1)  # h direction
print(axis0)
print(axis1)
