#!usr/bin/python3
from picamera2 import Picamera2, Preview
import cv2
from ultralytics import YOLO
import numpy as np
from send_data import *
from random_folder_generator import *

#create random folder
random_folder = get_random_bytes(4)  # Get 4 random bytes
create_directory("/mnt/hd1", random_folder) 

counter = 0 #simple counter for storing images

#camera configs
camera = Picamera2()
width = 640
height = 480
camera.configure(camera.create_video_configuration(main={"format" : 'RGB888', "size" : (width, height)})) #create custom config, for easy integration with opencv and the model
pic_config = camera.create_still_configuration() #use default config, it already has max resolution
camera.start() #initialize camera

#import the model
model=YOLO("/home/Captain/project/best_cross_val.pt")

#make a counter function from the results of the model
def count_values(arr):
    counts = np.bincount(arr, None, 4) #np bincount is the most efficient counter in Python
    form_str = "S{},M{},P{}".format(counts[1], counts[2], counts[3]) #string formatting for easy data extraction 
    return form_str

#main event loop
while True:
    frame = camera.capture_array("main") #read camera as np array, use main configuration
    results = model.predict(source=frame, imgsz=640, conf=0.5, classes=[1,2,3]) #use model on the captured frame
    class_ids=np.zeros(1, dtype=np.int64) #create an empty array to store detected class IDs
    for result in results:
        boxes = result.boxes.cpu().numpy() #translate Tensors to numpy arrays, make sure to use CPU
        print(boxes.cls) #debug boxes.cls
        print(boxes.cls.size) #debug boxes.cls
        if boxes.cls.size > 0: #check boxes.cls.size for detections
            #frame_ = results[0].plot() #load annotated picture (with bounding boxes, class names and confidence scores)
            #cv2.imshow('frame', frame_) #show annotated picture
            raw_frame = cv2.imwrite("/mnt/hd1/{folder}/frame_{counter}.jpg".format(folder=random_folder,counter = counter), frame)
            pic = camera.switch_mode_and_capture_file(pic_config,"/mnt/hd1/{folder}/{counter}.jpg".format(folder=random_folder,counter = counter))
            counter += 1
            class_ids = boxes.cls.astype(int) #copy the boxes.cls to the class_ids array
            print(count_values(class_ids)) #check message that will be sent over LoRaWAN
            ser = open_serial()
            send_message(ser, 0, 0, count_values(class_ids))
            print(wait_response(ser, 1))
            time.sleep(10) #pause the entire loop for 10s
        continue

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

camera.stop() #properly close the camera
cv2.destroyAllWindows() #properly close opencv generated windows (only applicable in GUI testing)
