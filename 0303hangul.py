import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
img = np.full((500, 1000, 3), 255, dtype=np.uint8)
#########
# sans-serif small #
# cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0))
#
# cv2.putText(img, "아름다운 강산-김준혁", (50, 200), \
#             cv2.FONT_HERSHEY_PLAIN, 4, (0, 0,0))
##########
# 이미지를 Pillow 이미지로 변환
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(img_pil)

# 한글 폰트 경로
font_path = 'C:/Windows/Fonts/gulim.ttc'

# 한글 폰트 로드
font = ImageFont.truetype(font_path, 40)

# 한글로 텍스트 작성
draw.text((50, 30), "Plain", fill=(0, 0, 0), font=font)
draw.text((50, 200), "아름다운 강산-김준혁", fill=(0, 0, 0), font=font)

# 이미지를 OpenCV 이미지로 변환
img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()