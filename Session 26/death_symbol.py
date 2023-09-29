import cv2
import numpy as np

# Load an image or create a blank one
amirmohammad_img = cv2.imread("Session 26/src/Amirmohammad.jpg")

start_point = (0, 150)
end_point = (150, 0)
line_color = (0, 0, 0)
line_thickness = 20

amirmohammad_img_whit_death_symbol = cv2.line(amirmohammad_img, start_point, end_point, line_color, line_thickness)

cv2.imshow('death symbol', amirmohammad_img_whit_death_symbol)
cv2.waitKey()