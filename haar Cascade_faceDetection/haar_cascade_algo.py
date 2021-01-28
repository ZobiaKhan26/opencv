import cv2

# Loading the image to be tested
test_image = cv2.imread('image1.jpg')

# Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def detect_faces(cascade, test_image, scaleFactor=1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    # convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 15)
    return image_copy


img = detect_faces(haar_cascade_face, test_image)
cv2.imshow("image",convertToRGB(img))
cv2.waitKey(0)
