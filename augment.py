import os
import random
import matplotlib as plt
from matplotlib import image, _image
import cv2
import numpy as np

folder = "./cats/1/"
path = 'cats'
pathLabels = 'labels.csv'
testRatio = 0.2
valRatio = 0.2
imageDimensions = (320, 320, 3)
WIDTH = 320
HEIGHT = 320

count = 1
images = []
# classNo = []
myList = os.listdir(path)
print("Total number of classes detected: ", len(myList))
noOfClasses = len(myList)
print("Importing Classes...")
for x in range(00, noOfClasses):
    myPicList = os.listdir(path + "/" + str(count))
    # print(myPicList)
    for y in myPicList:
        curImg = cv2.imread(path + "/" + str(count) + "/" + y)
        curImg = cv2.resize(curImg, (imageDimensions[0], imageDimensions[1]))
        images.append(curImg)
        # classNo.append(count)
    print(count, end="  ")
    count = count + 1
print("  ")
print("Total images in the image list: ", len(images))

# Select 2 images randomly for augmentation

sample_img = random.choices(images, k=4)  # Choose any 4 random images
# sample_img = np.array(sample_img)
sample_img = list(sample_img)
img = sample_img
# print(img)
img1 = sample_img[0]
img2 = sample_img[1]
img3 = sample_img[2]
img4 = sample_img[3]

# Image Augmentation

# Shifting Down
for j in range(WIDTH, 1, -1):  # Consider total width
    for i in range(imageDimensions[0]):
        if imageDimensions[0] > j > 50:  # 320 from below and 50 from above
            img1[j][i] = img1[j - 50][i]

cv2.imwrite(os.path.join(folder, '7.jpg'), img1)
cv2.waitKey(0)
print('Shifted down')

# Shifting Right
for j in range(WIDTH):
    for i in range(HEIGHT):
        if i < HEIGHT - 50:
            img2[j][i] = img2[j][i + 20]

cv2.imwrite(os.path.join(folder, '8.jpg'), img2)
cv2.waitKey(0)
print('Shifted right')

# Rotation
img3 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(os.path.join(folder, '9.jpg'), img3)
cv2.waitKey(0)
print('Rotated 90 degrees')
img4 = cv2.rotate(img4, cv2.ROTATE_180)
cv2.imwrite(os.path.join(folder, '10.jpg'), img4)
cv2.waitKey(0)
print('Rotated 180 degrees')
