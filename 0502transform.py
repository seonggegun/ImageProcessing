import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
cv2.imshow("",img)

dx = 100; dy = 50
mtrx = np.float32([[1,0,dx], [0,1,dy]])
height, width, _ = img.shape
dst = cv2.warpAffine(img, mtrx, (width+dx, height+dy))

cv2.imshow("",img)
cv2.imshow("p", dst)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

mtrx = np.float32([[2,0,0], [0,3,0]])
height, width, _ = img.shape
dst = cv2.warpAffine(img, mtrx, (width * 2, height * 3))

cv2.imshow("",img)
cv2.imshow("p", dst)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

mtrx = np.float32([[0.5,0,0], [0,0.8,0]])
height, width, _ = img.shape
dst = cv2.warpAffine(img, mtrx, (int(width * 0.5)+1, int(height * 0.8)+1))

cv2.imshow("",img)
cv2.imshow("p", dst)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()


dst = cv2.resize(img, (500, 500))

cv2.imshow("",img)
cv2.imshow("p", dst)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#------------------------------------------------
import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
dst = cv2.resize(img, (int(width * 0.7), int(height * 0.8)))
cv2.imshow("",img)
cv2.imshow("resize", dst)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()