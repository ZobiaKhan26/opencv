import cv2
import matplotlib as plt
from matplotlib import pyplot
from sklearn.externals._pilutil import imread

img_dim = (350, 350)
# show original image
orig_img = cv2.imread("image1.jpg")
cv2.imshow("Original image", orig_img)
# Convert to HSV
hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image", hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gray Scale image
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray_img)

# Static Threshold images
th_gray = imread("gray.jpg", 0)
ret, th1 = cv2.threshold(th_gray, img_dim[0], img_dim[1], cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(th_gray, img_dim[0], img_dim[1], cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(th_gray, img_dim[0], img_dim[1], cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(th_gray, img_dim[0], img_dim[1], cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(th_gray, img_dim[0], img_dim[1], cv2.THRESH_TOZERO_INV)
th_names = ["original image", "Binary", "Binary invert", "Truncate", "ToZero", "ToZero Invert"]
img_ths = [th_gray, th1, th2, th3, th4, th5]
labels = [1, 2, 3, 4, 5, 6]
for i in range(6):
    plt.pyplot.subplot(2, 3, i + 1),
    plt.pyplot.imshow(img_ths[i], 'gray', vmin=0, vmax=255)
    plt.pyplot.title(th_names[i])
    plt.pyplot.xticks([]), plt.pyplot.yticks([])
plt.pyplot.show()




