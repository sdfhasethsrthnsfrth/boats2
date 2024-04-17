#!usr/bin/python
import serial
import time

port = "/dev/ttyS0" #should be correct serial port I hopes
baudrate = 115200
time_out = 5 #timeout for listening in ms, doesn't do much tbh
ser = serial.Serial(port, baudrate, timeout=1) #keep timeout for sending low
ser.flushInput()
ser.flushOutput()

def wait_response(serial_port, time_out):
	response=""
	start = time.time()*1000
	while True:
		current_millis = time.time()*1000
		if serial_port.in_waiting or (current_millis - start) < time_out:
			msg = serial_port.readline().decode()
			response += msg
		else:
			break
	return response

def send_command(command):
    time.sleep(0.1)
    ser.write(("AT+" + command + "\r\n").encode())
    
#send a testframe of data
send_command("DTRX=0,0,20,AF123AF123AF123AF123")
print(wait_response(ser, 1))

#this should return:
#"OK+SEND:0A"
#"OK+SENT:08"

send_command("DRX?")
try:
    while True:
        if ser.in_waiting > 0:
            message = ser.readline().decode()
            print("message ", message)
except KeyboardInterrupt:
    print("bye bye")
ser.close()
