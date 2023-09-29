import cv2

man_img = cv2.imread("Session 26/src/2.jpg")
inverted_man_img = 255 - man_img

woman_img = cv2.imread("Session 26/src/1.jpg")
inverted_woman_img = 255 - woman_img

cv2.imshow("man", inverted_man_img)
cv2.imshow("woman", inverted_woman_img)
cv2.waitKey()

