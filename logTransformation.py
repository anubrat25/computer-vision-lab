import cv2
import numpy as np

img = cv2.imread('/Users/anubratbora/Desktop/beach.jpg')
c = 20

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
log_img = c * np.log(1 + gray_img.astype(np.float64))
log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX)
log_img = np.uint8(log_img)

result = cv2.hconcat([gray_img, log_img])

cv2.imwrite('log_img.jpg', result)
cv2.imshow('log_img', log_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
