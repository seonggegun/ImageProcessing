import cv2
import numpy as np
img = cv2.imread('./img/gaussian_noise.jpg')

kernel = np.ones((5,5))/25
blured = cv2.filter2D(img, -1, kernel)
cv2.imshow("origin", img)
cv2.imshow("blured", blured)
cv2.waitKey(0)
cv2.destroyAllWindows()

k1 = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]]) / 16

blur1 = cv2.filter2D(img, -1, k1)
cv2.imshow("origin", img)
cv2.imshow("blur1", blur1)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur2 = cv2.medianBlur(img, 3)
blur3 = cv2.bilateralFilter(img, 5, 75, 75)
cv2.imshow("origin", img)
cv2.imshow("gasussian", blur1)
cv2.imshow("meidan", blur2)
cv2.imshow("bilateral", blur3)

#gaussian filter library 사용
# blur2 = cv2.GaussianBlur(img, (3,3), 0)
# cv2.imshow("origin", img)
# cv2.imshow("blur2", blur2)
# cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()