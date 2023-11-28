import cv2
import cv2.gapi.wip.draw
import numpy as np

img_face = cv2.imread('./img/man_face.jpg')
img_skull = cv2.imread('./img/skull.jpg')

height, width, depth = img_face.shape
height, width = img_face.shape[:2]
height, width, depth = img_face.shape

middle = width // 2

img = np.zeros_like(img_face)
img[:, :middle, :] = img_face[:, :middle,:].copy()
img[:, middle:, :] = img_skull[:, middle:, :].copy()

alpha_width_rate = 50
alpha_width = width * alpha_width_rate // 100 # 알파 블렌딩 범위
start = middle - alpha_width // 2 # 알파 블렌딩 시작 지점
step = 100/ alpha_width # 알파 값 간격

for i in range(alpha_width + 1):
    alpha = (100 - step * i) / 100 # 증감 간격에 따른 알파 값(1~0)
    beta = 1 - alpha # 베타값 (0~1)
    #알파 블렌딩 적용
    img[:, start + i] = img_face[:, start + i] * \
                             alpha + img_skull[:, start + i] * beta
    print(i, alpha, beta)

cv2.imshow("face", img_face)
cv2.imshow("skull", img_skull)
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()