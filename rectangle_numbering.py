# Importing OpenCV library
import cv2 as cv

# Loading input image
img = cv.imread('Input_Image.png')

# Converting image into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Performing Canny edge detection 
edges = cv.Canny(gray, 100, 200)

# Finding contours
contours, hierarchy = cv.findContours(
    edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Counting Labels 
numbers = ["1", "4", "2", "3"]

# Iterating over contours and labeling rectangles
for i, contour in enumerate(contours):
    # Approximating polynomial curves
    epsilon = 0.01 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    # Checking for rectangles
    if len(approx) == 4:
        # Green rectangle
        cv.drawContours(img, [contour], -1, (0, 255, 0), 3)
        x, y, w, h = cv.boundingRect(contour)
        cv.putText(img, numbers[i], (x, y - 0),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Displaying image
cv.imshow('output', img)

# Saving Images
cv.imwrite('Output_Rectangle_Image_count.png', img)
cv.imwrite('Output_Edge_Detection_Image.png', edges)


cv.waitKey(0)
cv.destroyAllWindows()