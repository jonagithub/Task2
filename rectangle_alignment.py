# Importing libraries
import cv2 as cv
import numpy as np

# Reading and extracting rectangles from an image
image = cv.imread('Input_Image.png')
# Creating a new NumPy array of the same size and data type as the 'image' array initializing all its values to zeros and assigning it to output_image
output_image = np.zeros_like(image)

# Extracts four rectangle regions from the image array using format [start_row:end_row, start_col:end_col]
rectangle_1 = image[200:500, 300:700]
rectangle_2 = image[0:200, 0:250]
rectangle_3 = image[0:200, 300:600]
rectangle_4 = image[200:600, 0:300]


# Rotation function
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# Rotating rectangles and displaying them
rectangle_1 = rotate(rectangle_1, 30)
cv.imshow('Rectangle 1', rectangle_1)

rectangle_2 = rotate(rectangle_2, 15)
cv.imshow('Rectangle 2', rectangle_2)

rectangle_3 = rotate(rectangle_3, -15)
cv.imshow('Rectangle 3', rectangle_3)

rectangle_4 = rotate(rectangle_4, -30)
cv.imshow('Rectangle 4', rectangle_4)


# Aligning rectangles and saving images
output_image[200:500, 300:700] = rectangle_1
output_image[0:200, 0:250] = rectangle_2
output_image[0:200, 300:600] = rectangle_3
output_image[200:600, 0:300] = rectangle_4
cv.imshow('Aligned_rectangle',output_image)

cv.imwrite('Straight_Rectangle.png', output_image)
cv.imwrite('Straight_Rectangle_1.png', rectangle_1)
cv.imwrite('Straight_Rectangle_2.png', rectangle_2)
cv.imwrite('Straight_Rectangle_3.png', rectangle_3)
cv.imwrite('Straight_Rectangle_4.png', rectangle_4)

cv.waitKey(0)
cv.destroyAllWindows()