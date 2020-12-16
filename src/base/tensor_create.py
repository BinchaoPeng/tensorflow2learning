import tensorflow as tf
import numpy as np

# dim=1 with 2 elements
a = tf.constant([2, 4], dtype=tf.int64)
print(a)
print(a.dtype)
print(a.shape)

# numpy to tensor
nparr = np.array([1, 2, 3])
b = tf.convert_to_tensor(nparr)
c = tf.convert_to_tensor(nparr, dtype=tf.float64)
print(nparr)
print(b)
print(c)

# tensor filled with 0
zeros = tf.zeros([3, 3])
print(zeros)

# tensor filled with 1
ones = tf.ones([3, 3])
print(ones)

# tensor filled with specific value
fill = tf.fill([3, 3], 9)
print(fill)

# create random with normal,default: mean=0,std=1
ran = tf.random.normal([3, 3, 3], mean=1, stddev=1)
print(ran)

# create random with truncated normal, random value is belonged to (mean-2std,mean+2std)
tru = tf.random.truncated_normal([3, 3, 3])
print(tru)

# create tensor with uniform, random value is belonged to [minval,maxval]
uni = tf.random.uniform([2,2,2], maxval=5, minval=3)
print(uni)
