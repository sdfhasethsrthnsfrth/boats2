from ultralytics import YOLO
import cv2 as cv
from picamera2 import Picamera2
import numpy as np

#camera and video encoder specifics
camera = Picamera2() #initialize camera
video_config = camera.create_still_configuration() #configuration settings for resolutions
camera.configure(video_config) #set configurations
#encoder = H264Encoder(bitrate=10000000) #use .h264 encoder for making recordings
output = "" #placeholder for the output file
camera.start() #load the default config for exposure time etc, mostly testing purposes

model = YOLO('best_cross_val.pt') #load custom model

#main loop

frame = camera.capture_array() #get camera image as byte
img = cv.imread(frame)
cv.imshow("img", img)
results = model(img) #use model on captured frame
  

names_dict = results[0].names #extract names of all classes
probs = results[0].probs.toList() #extract probability of class from the image
predicted_class = names_dict[np.argmax(probs)] #show name of class with highest probability

camera.stop()
cv.destroyAllWindows()
