import cv2

img = cv2.imread("/Users/anubratbora/Desktop/cv.jpg")
if img is None:
    print("Error: Image not found or unable to load.")
else:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
