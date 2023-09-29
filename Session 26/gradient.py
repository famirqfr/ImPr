import numpy as np
import cv2

rows, cols = 512, 512

gradient = np.linspace(255, 0, cols, dtype=np.uint8)
gradient = np.transpose(np.tile(gradient, (rows,1)))

cv2.imshow("gradient", gradient)
cv2.waitKey()

