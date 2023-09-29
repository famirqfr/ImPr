import numpy as np
import cv2

rows = 8
cols = 8
square_size = 75

chess_board = np.ones(
    (rows * square_size, cols * square_size, 3)) * 255

for row in range(rows):
    for col in range(cols):
        if (row+col) % 2 == 0:
            chess_board[row * square_size:(row + 1) * square_size,
                        col * square_size:(col + 1) * square_size] = [255, 255, 255]
        else:
            chess_board[row * square_size:(row + 1) * square_size,
                        col * square_size:(col + 1) * square_size] = [0, 0, 0]

cv2.imshow("chessboaed", chess_board)
cv2.waitKey()
