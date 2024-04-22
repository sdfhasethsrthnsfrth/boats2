from ultralytics import YOLO
import cv2 as cv
from picamera2 import Picamera2
import numpy as np

#camera and video encoder specifics
camera = Picamera2() #initialize camera
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores") #configuration settings for resolutions
picam2.configure(video_config) #set configurations
encoder = H264Encoder(bitrate=10000000) #use .h264 encoder for making recordings
output = "" #placeholder for the output file
camera.start() #load the default config for exposure time etc, mostly testing purposes

model = YOLO('/path/to/best.pt') #load custom model

#main loop
while True:
  frame = picam2.capture_array() #get camera image as byte array


results = model.predict('/path/to/imagefile') #use model on captured frame


cap = cv2.VideoCapture(0) 
# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera")
    exit()

# Capture frames from the camera
while True:
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Couldn't capture frame")
        break

    # Display the frame
    cv2.imshow('Raspberry Pi Camera', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
names_dict = results[0].names #extract names of all classes
probs = results[0].probs.toList() #extract probability of class from the image
predicted_class = names_dict[np.argmax(probs)] #show name of class with highest probability

picam2.stop()
cv2.destroyAllWindows()
