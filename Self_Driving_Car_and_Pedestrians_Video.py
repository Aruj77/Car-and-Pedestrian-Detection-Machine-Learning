import cv2

trained_data_cars = cv2.CascadeClassifier('car_detector.xml')
trained_data_pedestrians = cv2.CascadeClassifier('haarcascade_fullbody.xml')

video = cv2.VideoCapture('Tesla_video2.mp4')


while True:
    read_successful, frame = video.read()
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_cars =  trained_data_cars.detectMultiScale(grayscale_frame)
    detect_pedestrians =  trained_data_pedestrians.detectMultiScale(grayscale_frame)
    for (x,y,h,w) in detect_cars:
        cv2.rectangle(frame, (x, y), (x+h, y+w), (0, 255, 0), 2)
    for (x,y,h,w) in detect_pedestrians:
        cv2.rectangle(frame, (x, y), (x+h, y+w), (0, 255, 255), 2)
    cv2.imshow('Video Car Detection by Aruj Bansal', frame  )
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

video.release()