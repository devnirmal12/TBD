import cv2

image = cv2.imread("../photos/cats 2.jpg")

if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

