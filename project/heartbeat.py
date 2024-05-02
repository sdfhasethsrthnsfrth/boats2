#!/usr/bin/bash/python3 
from send_data import *

#this script repeats every 15 minutes as a cronjob
ser = open_serial() #open serial port
send_message(ser, 0, 0, "0x00") #send heartbeat as "0"