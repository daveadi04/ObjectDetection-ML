from ultralytics import YOLO
import cv2
import cvzone

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

while True:
  success, img = cap.read()
  cv2.imshow("Image", img)
  cv2.waitKey(1)