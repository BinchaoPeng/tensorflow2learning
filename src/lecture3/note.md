[TOC]

# lecture3.1-搭建网络八股sequential

![image-20201217154234760](images/image-20201217154234760.png)

Sequential：逐层描述网络，前向传播

compile：配置训练方法，优化器、损失函数、评测指标

fit：执行训练过程，告知训练集和测试集的输入特征和标签，batch、epoch的大小、

summary：打印网络结构和参数统计



## train test

两种方式：

- 手动划分训练集和测试集
-  在fit（）中使用比例参数划分，如`validation_split=0.2`



## Sequential-容器

![image-20201217154701112](images/image-20201217154701112.png)

Flatten：输入特征转变为一维数组



## compile

![image-20201217154914369](images/image-20201217154914369.png)

from_logits:表示预测结果是否是经过概率分布（比如softmax）



## fit

![image-20201217155338135](images/image-20201217155338135.png)



## summary

![image-20201217155432817](images/image-20201217155432817.png)



# lecture3.2搭建网络八股class

![image-20201217165354400](images/image-20201217165354400.png)

![image-20201217165413785](images/image-20201217165413785.png)



![image-20201217165633768](images/image-20201217165633768.png)

class中必须实现init和call函数，init中定义网络结构，call实现前向传播。

## demo MNIST

![image-20201217165852975](images/image-20201217165852975.png)

![image-20201217165913727](images/image-20201217165913727.png)

### Sequential实现

![image-20201217170113345](images/image-20201217170113345.png)

归一化，变为0-1，更有利于神经网络吸收



## class实现

![image-20201217170429008](images/image-20201217170429008.png)