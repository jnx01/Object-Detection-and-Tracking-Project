import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")
tracker=[]
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blueframe=cv2.GaussianBlur(gray,(17,17),0)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(blueframe, cv2.HOUGH_GRADIENT, 1.2, 100,
                               param1=100, param2=30,
                               minRadius=80, maxRadius=90)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
                center = (i[0], i[1])
                tracker.append((i[0], i[1]))
                radius = i[2]
                cv2.circle(frame, center, radius, (0, 0, 255), 6)

    for i in tracker :
        cv2.circle(frame, i, 0, (200, 120, 35), 15)

    cv2.imshow("Circular Object Path Detection",cv2.flip(frame,1))
    c = cv2.waitKey(1)
    if c == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
