import cv2
import numpy as np

#  create the empty canvas for drawing
canvas = np.zeros((300, 300, 3),dtype='uint8')

# draw a green line
green = (0, 255, 0)
cv2.line(canvas,(0,0), (150, 150), green,5)

# draw a rectangle
white = (255, 255, 255)
cv2.rectangle(canvas,(0, 100),(200, 250),white,-1)

# draw a colored circle at the center of the canvas
centerx = canvas.shape[1] // 2
centery = canvas.shape[0] // 2
color = (125, 67, 79)

cv2.circle(canvas,(centerx, centery), 70, color, -1)

cv2.imshow("Image", canvas)
cv2.waitKey(0)