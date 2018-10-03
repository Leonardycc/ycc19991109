* web可以直接的的驱动摄像头
* usb_cam
* uvc_cam
* libuvc_cam
* cv_cam
* 导入库
* • import numpy as np
* • import cv2
* 读入图片
* • img = cv2.imread('messi5.jpg’,0)
* 显示图片
* • cv2.imshow('image',img)
* 等待时间
* • k = cv2.waitKey(0)
* 绘制直线
* • cv2.line(img,(0,0),(511,511),(255,0,0),5) 
* 绘制矩形
* • cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
* 绘制圆
* • cv2.circle(img,(447,63), 63, (0,0,255), -1)
* 绘制椭圆
* • cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
