#!/usr/bin/python3 
from send_data import *
import logging

logging.basicConfig(filename='/home/Captain/project/heartbeatlog/heartbeat.log', 
                  level=logging.INFO
                  format='%(asctime)s - %(levelname)s - %(message)s')

#this script repeats every 15 minutes as a cronjob
try:
  ser = open_serial() #open serial port  
  logging.info("Serial port opened")

  send_message(ser, 0, 0, "\x00") #send heartbeat as "00"
  logging.info("Heartbeat sent")
#  print(wait_response(ser, 1))
except Exception as e:
  logging.error(f"An error occured: {e}")
