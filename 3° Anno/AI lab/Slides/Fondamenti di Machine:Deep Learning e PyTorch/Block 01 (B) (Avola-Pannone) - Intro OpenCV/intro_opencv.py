import cv2

img = cv2.imread("3° Anno/AI lab/2025-2026/Slides/Fondamenti di Machine:Deep Learning e PyTorch/Block 01 (B) (Avola-Pannone) - Intro OpenCV/Data/ezio.jpg")

# print some image information
print(f'The width of the image is {img.shape[1]} pixels')
print(f'The height of the image is {img.shape[0]} pixels')
print(f'The number of channels of the image is {img.shape[2]}')

# show the image on screen
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows() #only needed for jupyter notebok

# access to a pixel of the image
(r, g, b) = img[0, 0]

print(f'Pixel at 0,0: Red {r}, Green {g}, Blue {b}')

# change the value of the pixel
img[0, 0] = (0, 0, 0)

# access to a portion of the image
corner = img[0 : 100, 0 : 100]

# change the color of the pixel of a portion
img[0 : 100, 0 : 100] = (0, 255, 0)


cv2.imshow("Image", img)
cv2.waitKey(0)