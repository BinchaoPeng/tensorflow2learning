[TOC]

# lecture4.1-搭建网络八股总览

![image-20201217171117659](images/image-20201217171117659.png)

![image-20201217171127632](images/image-20201217171127632.png)

# lecture4.2-自制数据集

![image-20201217171352943](images/image-20201217171352943.png)



![image-20201217171606375](images/image-20201217171606375.png)

from PIL import Image

## 完整代码

![image-20201217171751477](images/image-20201217171751477.png)



![image-20201217171817817](images/image-20201217171817817.png)



# lecture4.3-数据增强

![image-20201217172154039](images/image-20201217172154039.png)



![image-20201217172258360](images/image-20201217172258360.png)

（60000，28，28，1）这个多出来的1，指的是通道数



# lecture4.3-断点续训

![image-20201217173248255](images/image-20201217173248255.png)



xxx.ckpt是模型文件；xxx.index是生成模型时同步生成的索引表

## demo

![image-20201217173504232](images/image-20201217173504232.png)

history可以使下次训练时，接着上次继续训练

# lecture4.5-参数提取

![image-20201217173710455](images/image-20201217173710455.png)

## demo

![image-20201217173805319](images/image-20201217173805319.png)



# lecture4.6-acc/loss可视化

![image-20201217174148800](images/image-20201217174148800.png)



![image-20201217174301398](images/image-20201217174301398.png)



# lecture4.7-给图识物

![image-20201217203534761](images/image-20201217203534761.png)



