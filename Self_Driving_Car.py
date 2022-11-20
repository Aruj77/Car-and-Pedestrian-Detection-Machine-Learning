import cv2

img = cv2.imread('car_image.jpg')


car_tracker = cv2.CascadeClassifier('car_detector.xml')

# grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detect_cars = car_tracker.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

for (x,y,h,w) in detect_cars:
    cv2.rectangle(img, (x, y), (x+h, y+w), (0, 255, 0), 2)

cv2.imshow('Car Detection by Aruj Bansal', img)
cv2.waitKey()

print('Code Completed')