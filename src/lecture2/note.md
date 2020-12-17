[TOC]

# lecture 2.1

## tf.where()

![image-20201217141527957](images/image-20201217141527957.png)



## np.random.Randomstate.rand()

![image-20201217141648909](images/image-20201217141648909.png)



## np.vstack()

![image-20201217141738535](images/image-20201217141738535.png)



## np.mgrid[]  .ravek()	np.c_[]	网格

![image-20201217141845377](images/image-20201217141845377.png)



# lecture2.2



## NN复杂度

![image-20201217142225993](images/image-20201217142225993.png)



## 指数衰减学习率

![image-20201217142453761](images/image-20201217142453761.png)



# lectuer2.3-激活函数

## sigmoid函数

**梯度消失：**

​	神经网络需要逐层链式求导，即多层导数，连续相乘，其中会有多个为0或趋于零，使得结果趋于0，导致参数无法更新。

![image-20201217144841093](images/image-20201217144841093.png)



## Tanh函数

![image-20201217144934824](images/image-20201217144934824.png)



## Relu函数

![image-20201217145139285](images/image-20201217145139285.png)



## Leaky Relu函数

![image-20201217145259547](images/image-20201217145259547.png)



## 总结

![image-20201217145325548](images/image-20201217145325548.png)



# lecture2.4-损失函数



- 均方误差
- 自定义
- 交叉熵

![image-20201217150008405](images/image-20201217150008405.png)

![image-20201217150727060](images/image-20201217150727060.png)

![image-20201217150815762](images/image-20201217150815762.png)

距离越近表示越接近。

### softmax和交叉熵结合使用

![image-20201217151050070](images/image-20201217151050070.png)

y_pro.....和loss_ce1....两步等同于loss_ce2.....



# lecture2.5-缓解过拟合



![image-20201217151448479](images/image-20201217151448479.png)

## 正则化

![image-20201217151532851](images/image-20201217151532851.png)



# lecture2.6-优化器

![image-20201217152431482](images/image-20201217152431482.png)

不同的优化器实质上只是定义了不同的一阶动量和二阶动量表达式

## SGD随机梯度下降

![image-20201217152722945](images/image-20201217152722945.png)

## SGDM

![image-20201217152932738](images/image-20201217152932738.png)

改变了一阶动量mt



## Adagrad

![image-20201217153231374](images/image-20201217153231374.png)

## RMSProp

![image-20201217153510921](images/image-20201217153510921.png)



## Adam

![image-20201217153641513](images/image-20201217153641513.png)



