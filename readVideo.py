import cv2
cap = cv2.VideoCapture("/Users/anubratbora/Desktop/855289-hd_1920_1080_25fps.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()