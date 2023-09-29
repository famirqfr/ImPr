import cv2

sad_man_img = cv2.imread("Session 26/src/3.jpg")
happy_man_img = cv2.rotate(sad_man_img, cv2.ROTATE_180)

cv2.imshow("happy man", happy_man_img)
cv2.waitKey()

