import cv2

img=cv2.imread('/home/intel/Desktop/image.jpeg',0)

cv2.imshow("Display",img)

cv2.waitKey(1000)

cv2.imwrite("imagegray.jpeg",img)

cv2.destroyALLWindows()
