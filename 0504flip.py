import cv2
import numpy as np

# 10도회전
img = cv2.imread('./img/children.jpg')

height, width = img.shape[0:2]
d10 = 10 * np.pi / 180
fl1 = np.float32([[-1, 0, width-1],
                  [0, 1, 0]])
fl2 = np.float32([[-1, 0, width-1],
                  [0, -1, height -1]])
r10 = cv2.warpAffine(img, fl1, (width, height))
r12 = cv2.warpAffine(img, fl2, (width, height))
cv2.imshow("",img)
cv2.imshow("flipx", r10)
cv2.imshow("flipxy", r12)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#흑백 좌우반전
imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipx = np.zeros_like(imgg)
for i in range(width):
    dflipx[: , i] = imgg[:, width-i-1]

cv2.imshow("org",imgg)
cv2.imshow("dflipx",dflipx)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#흑백 상하반전
imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
duplex = np.zeros_like(imgg)
for i in range(height):
    duplex[i, :] = imgg[height-i-1, :]

cv2.imshow("org",imgg)
cv2.imshow("duplex",duplex)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#과제 흑백 상하반전

from PIL import ImageFont, ImageDraw, Image

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipx = np.zeros_like(imgg)
for i in range(width):
    dflipx[: , i] = imgg[:, width-i-1]

duplex = np.zeros_like(imgg)
for i in range(height):
    duplex[i, :] = imgg[height-i-1, :]

cv2.imshow("org",imgg)
cv2.imshow("dflipx",dflipx)
cv2.imshow("duplex",duplex)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

####
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
height, width = imgg.shape[:2]

dflipx = np.zeros_like(imgg)
for i in range(width):
    dflipx[:, i] = imgg[:, width-i-1]

duplex = np.zeros_like(imgg)
for i in range(height):
    duplex[i, :] = imgg[height-i-1, :]

cv2.imshow("org", imgg)
cv2.imshow("dflipx", dflipx)
cv2.imshow("duplex", duplex)

image_pil = Image.fromarray(imgg)
draw = ImageDraw.Draw(image_pil)

font_path = 'C:/Windows/Fonts/gulim.ttc'
font_size = 20
font = ImageFont.truetype(font_path, font_size)

korean_text = "김준혁"
text_position = (width - 200, height - 50)
draw.text(text_position, korean_text, font=font, fill=255)

img_with_text = np.array(image_pil)
cv2.imshow("org_with_text", img_with_text)

cv2.waitKey(0)
cv2.destroyAllWindows()