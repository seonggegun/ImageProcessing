# 2023.11.7 이미지처리수업
# 이미지 연산 - 뺴기연산
import numpy as np
import cv2

img1 = cv2.imread('./img/robot_arm1.jpg')
img2 = cv2.imread('./img/robot_arm2.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
diff = cv2.absdiff(img1_gray, img2_gray)

otsu_threshold, t_diff = cv2.threshold(diff, -1, 255, cv2.THRESH_BINARY
                                       | cv2.THRESH_OTSU)

diff_color = cv2.cvtColor(t_diff, cv2.COLOR_BGR2RGB)
diff_color[:, :, 0] = 0
spot = cv2.bitwise_xor(img1, diff_color)

cv2.imshow("img1", img1_gray)
cv2.imshow("img2", img2_gray)
cv2.imshow("diff", diff)
cv2.imshow("tdiff", t_diff)
cv2.imshow("diff_color", diff_color)
cv2.imshow(("sdpot", spot))
cv2.waitKey()
cv2.destroyAllWindows()
