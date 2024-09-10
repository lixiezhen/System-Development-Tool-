from PIL import Image
from pylab import *
import matplotlib
matplotlib.use('TkAgg')
# 读取图像到数组中
im = array(Image.open('image-20221226145619790.jpg'))
# 绘制图像
imshow(im)
# 一些点
x = [100,100,400,400]
y = [200,500,200,500]
# 使用红色星状标记绘制点
plot(x,y,'r*')
# 绘制连接前两个点的线
plot(x[:2],y[:2])
# 添加标题，显示绘制的图像
title('Plotting: "image-20221226145619790.jpg"')
show()