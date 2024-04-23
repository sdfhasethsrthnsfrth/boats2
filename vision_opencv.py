from ultralytics import YOLO
import cv2 as cv
import numpy as np
from send_data import *

cam_port = 0
video = VideoCapture(cam_port)
if not video.isOpened(): #check camera opened correctly
    print("Error: Couldn't open the camera")
    exit()
  
#parameters for VideoWriter (to create output file)
video_counter = 0 #placeholder for the output filename
frame_width = int(video.get(3)) #cast frame width to int
frame_height = int(video.get(4)) #cast frame height to int
size = (frame_width, frame_height) #set size as tuple of width and height
fps = 15 #set fps for the recording
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #use one of the mp4 encoders

#parameters for the machine vision model
model = YOLO('/path/to/best.pt') #load custom model

#parameters for frameskipping
frame_rate = int(video.get(5)) #cast fps to int
frame_counter = 0
frames_to_skip = frame_rate * 5 #skip 5 seconds of frames before reading a new one

while True:
	ret, frame = video.read()
  if not ret: #check frame was read correctly
		print("Error: Couldn't capture frame")
    	break
	frame_counter += 1
 if frame_counter >= frames_to_skip:
   #do machine vision
   #code
	 
   frame_counter = 0  # Reset frame counter after displaying the frame
 
  
  # Exit the loop if 'q' is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
results = model.predict('/path/to/imagefile') #use model on captured frame
names_dict = results[0].names #extract names of all classes
probs = results[0].probs.toList() #extract probability of class from the image
predicted_class = names_dict[np.argmax(probs)] #show name of class with highest probability

if video_counter == 1: #initialize VideoWriter if it is the first time
  video_name = f"video_{video_counter}.mp4" 
  out = cv2.VideoWriter(video_name, fourcc, fps, (output_width, output_height))
  video_counter +=1
  
video_name = f"video_{video_counter}.mp4" #
out.write(frame) # Write the recording to the video file if it is not the first time

out.release() #close instance of VideoWriter properly
video.release() #close instance of camera properly
cv2.destroyAllWindows() #shut down all opened windows (shouldn't be called in headless operation, but good practice anyway)
