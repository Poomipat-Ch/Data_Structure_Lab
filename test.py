import cv2


camera = cv2.VideoCapture(0)

while camera.isOpened():
    _,frame = camera.read()
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()