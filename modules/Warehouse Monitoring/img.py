# this module helps to extract frames of videos

# importing libraries
import cv2

cpt = 0  # counter
maxFrames = 10  # no. of frames of videos you want

cap = cv2.VideoCapture('sample4.mp4')
while cpt < maxFrames:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1020, 500))
    cv2.imshow("test window", frame)  # show image in window

    # to store the frames in the 'images' folder
    cv2.imwrite(r'D:\COLLEGE\FOURTH YEAR\Major Project\Warehouse Module\images\img_%d.jpg' % cpt, frame)
    cpt += 1
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
