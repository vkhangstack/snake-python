import cv2

# import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread("shapes.png")

# convert image to gray color
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


cv2.imshow("shapes", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
