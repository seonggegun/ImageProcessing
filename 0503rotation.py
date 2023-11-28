import cv2
import numpy as np

# 10도회전
img = cv2.imread('./img/fish.jpg')
height, width = img.shape[0:2]
d10 = 10 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), 0],
                  [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (width, height))
cv2.imshow("",img)
cv2.imshow("r10", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

# 90도 회전
img = cv2.imread('./img/fish.jpg')
height, width = img.shape[0:2]
d10 = 90 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), 256],
                  [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (width, height))
cv2.imshow("",img)
cv2.imshow("r90", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#180도 회전
img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 180 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), width],
                  [np.sin(d10), np.cos(d10), height]])
r10 = cv2.warpAffine(img, m10, (width, height))
cv2.imshow("",img)
cv2.imshow("r180", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()