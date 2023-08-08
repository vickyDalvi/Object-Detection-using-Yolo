from ultralytics import YOLO
import cv2

model = YOLO("../yolo-weights/yolov8l.pt")
results = model(r"D:\NitsVicky\BIA- (DATA ANALYTICS)\python\object detection project\Chapter 5 Running Yolo\kids-in-masks-getting-on-school-bus-1-1440x430.png", show = True)
cv2.waitKey(0)   #it stops the image for us to see