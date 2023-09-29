import cv2
import numpy as np

# Create a blank white image
width, height = 512, 512
background = np.ones((height, width, 3), dtype=np.uint8) * 255

line_color = (0, 0, 0)
line_thickness = 20

start_point_left_side = (256, 200)
end_point_left_side = (180, 350)

start_point_right_side = (256, 200)
end_point_right_side = (332, 350)

start_point_centeral_side = (210, 310)
end_point_centeral_side = (300, 310)

first_char_name = cv2.line(background, start_point_left_side, end_point_left_side, line_color, line_thickness)
first_char_name = cv2.line(background, start_point_right_side, end_point_right_side, line_color, line_thickness)
first_char_name = cv2.line(background, start_point_centeral_side, end_point_centeral_side, line_color, line_thickness)

cv2.imshow('Text Design', first_char_name)
cv2.waitKey(0)
cv2.destroyAllWindows()