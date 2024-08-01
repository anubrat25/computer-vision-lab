import cv2

img = cv2.imread('/Users/anubratbora/Desktop/mountains.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
neg = cv2.bitwise_not(gray)
cv2.imshow('Image', img)
cv2.imshow('Neg', neg)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('Neg.jpg', neg)
    cv2.destroyAllWindows()