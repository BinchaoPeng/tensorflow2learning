import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn import datasets

# 准备数据
iris = datasets.load_iris()
print(iris)
print(type(iris))
##	读入数据
x_data = iris.data
y_data = iris.target

##	数据集乱序
np.random.seed(666)
np.random.shuffle(x_data)
np.random.seed(666)
np.random.shuffle(y_data)

##	划分训练集、测试集
x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

print(type(x_train))
print(len(x_train))

x_train = tf.cast(x_train, dtype=tf.float32)
x_test = tf.cast(x_test, dtype=tf.float32)


##	构造【x，y】，设置batch
train_batch = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_batch = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

# 搭建网络
##	定义神经网络可训练参数
"""
input layer: 4
output layer: 3
"""
w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))

# 参数优化[train]
lr = 0.1
train_loss = []
test_acc = []
epoch = 500
loss_all = 0  # every epoch has 4 step,loss_all equals the addition of 4 step loss

##	循环迭代，使用with结构，梯度下降求导，loss

for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_batch):
        with tf.GradientTape() as tape:  # save gradient information
            y = tf.matmul(x_train, w1) + b1
            y = tf.nn.softmax(y)
            y_ = tf.one_hot(y_train, depth=3)
            loss = tf.reduce_mean(tf.square(y_ - y))
            loss_all += loss.numpy()  # finally get mean of loss_all
        # compute gradient
        grads = tape.gradient(loss, [w1, b1])

        # update weight
        w1.assign_sub(lr * grads[0])
        b1.assign_sub((lr * grads[1]))
    print("Epoch{},loss:{}".format(epoch, loss_all / 4))
    train_loss.append(loss_all / 4)
    loss_all = 0

    # 测试效果
    total_correct, total_number = 0, 0
    for x_test, y_test in test_batch:
        # make predictions with updated weight
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred = tf.argmax(y, axis=1)
        pred = tf.cast(pred, dtype=y_test.dtype)
        correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        total_correct += int(correct)
        total_number += x_test.shape[0]

    ## 计算acc
    acc = total_correct / total_number
    test_acc.append(acc)
    print("Test_acc:", acc)
    print("-----------------------------------------------")

# acc/loss可视化
## 	画图显示
### loss cruve
plt.title("loss cruve")
plt.xlabel('Epoch')
plt.ylabel("Loss")
plt.plot(train_loss, label="Loss")
plt.legend()  # 画出图线图标
plt.show()  # 画出图像

### acc cruve
plt.title("acc cruve")
plt.xlabel('Epoch')
plt.ylabel("acc")
plt.plot(test_acc, label="$Accuracy$")
plt.legend()  # 画出图线图标
plt.show()  # 画出图像
