import cv2

image = cv2.imread("../photos/cat.jpg")

if image is not None:
    cv2.imshow("Cat image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")