import cv2

img = cv2.imread("3° Anno/AI lab/2025-2026/Slides/Fondamenti di Machine:Deep Learning e PyTorch/Block 01 (B) (Avola-Pannone) - Intro OpenCV/Data/ezio.jpg")

# split img channels
(r,g,b) = cv2.split(img)

# merge the channel together wrongly
img2 = cv2.merge((b, b, b))

# get the first channel of the image
ch = img[:, :, 2]

cv2.imshow("Image",ch)
cv2.waitKey(0)