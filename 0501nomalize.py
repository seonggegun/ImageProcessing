import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 정규화
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# 원본 이미지 히스토그램 계산
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])

# 정규화된 이미지 히스토그램 계산
hist_normalized = cv2.calcHist([img_norm], [0], None, [256], [0, 256])

# 히스토그램 시각화
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image Histogram')
plt.plot(hist_original, color='b')

plt.subplot(1, 2, 2)
plt.title('Normalized Image Histogram')
plt.plot(hist_normalized, color='r')

plt.show()

# 이미지 및 히스토그램 창 표시
cv2.imshow("Original Image", img)
cv2.imshow("Normalized Image", img_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()