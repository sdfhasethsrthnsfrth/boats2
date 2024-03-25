#!usr/bin/python
import serial
import time

port = "/dev/ttyS0" #should be correct serial port I hopes
baudrate = 115200
time_out = 7000 #timeout for listening in ms, doesn't do much tbh
ser = serial.Serial(port, baudrate, timeout=1) #keep timeout for sending low
ser.flushInput()
ser.flushOutput()

def wait_response(serial_port, time_out):
	response=""
	start = time.time()*1000
	while True:
		current_millis = time.time()*1000
		if serial_port.in_waiting or (current_millis - start) < time_out:
			msg = serial_port.readline().decode().strip()
			response += msg
		else:
			print("breaking")
			break
	return response

#TO DO: use this fucntion to write cleaner code
def send_command(command):
    time.sleep(0.1)
    ser.write(("AT+" + command + "\r\n").encode())
    print(wait_response(ser, 7).decode())
#send_command("CJOINMODE=0")
#send_command("CDEVEUI=05B18B2C5428A0DA")
#send_command("CAPPEUI=0000000000000000")

#check connection by sending an empty AT command.
ser.write(b"AT\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return "+AT: OK"

#set Join Mode to OTAA (Over The Air Activation)
ser.write(b"AT+CJOINMODE=0\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#manually set DEVEUI to what the Digita network gave
ser.write(b"AT+CDEVEUI=05B18B2C5428A0DA\r\n") #16 byte address
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

ser.write(b"AT+CAPPEUI=0000000000000000\r\n") #16 byte address
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

#manually set APPKEY to what Digita network gave
ser.write(b"AT+CAPPKEY=00000000000000000000000000000000\r\n") #16 byte address
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

#manually set frequency band mask
ser.write(b"AT+CFREQBANDMASK=0001\r\n") #4 byte address
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

#manually set upload/downloadmode on different frequencies
ser.write(b"AT+CULDLMODE=2\r\n") #1 = same, 2 = different frequency
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

#manually set the workmode to "Normal"
ser.write(b"AT+CWORKMODE=2\r\n") #only this option is supported
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"


#for lowest energy consumption we will use this device as a class A
ser.write(b"AT+CCLASS=0\r\n") #0 = CLASS A, 1 = CLASS B, 2 = CLASS C
time.sleep(0.1)
print(wait_response(ser, 7))
#This should return: "OK"

#get battery level
ser.write(b"AT+CBL?\r\n") 
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "+CBL:x" with x = battery percentage
#if no battery is present this will return: "CBL:100"

ser.write(b"AT+CSTATUS?\r\n") 
time.sleep(0.1)
print(wait_response(ser, 7))
#status response overview
#00 = no data operation
#01 = data sending
#02 = data sending failed
#03 = data sending success
#04 join succes
#05 join fail
#06 netowkr may abnormal (res from Link Check)
#07 data sent success, no download
#08 data sent success, yes download

#Try to join the network with OTAA
ser.write(b"AT+CJOIN=1,1,10,8\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set up for uplink confirmation for messaging:
ser.write(b"AT+CCONFIRM=1\r\n") #1 =confirm, 0 = unconfirm uplink message
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set up application port
ser.write(b"AT+CAPPPORT=5\r\n") #decimal number in [1:223], 0x00 is reserved for LoRaWAN MAC command
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set up spreading factor and datarate
ser.write(b"AT+CDATARATE=5\r\n") #decimal number in [0:5], higher number = lower SF
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#inquire RSSI
ser.write(b"AT+CRSSI FREQBANDIDX?\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return a list x:<RSSI value> with x decimal number in [0:7]
#this lists the RSSI for all the frequency channels set previously with command "CFREQBANDMASK"

#Set number of trials for sending data
ser.write(b"AT+CNBTRIALS=1,3\r\n") #first number 1 = confirm, 0 = uncomfirm package, second number in range [1:15] sets number of trials
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set report mode
ser.write(b"AT+CTXP=0,0\r\n")#first number 0 = non periodic, 1 = periodic data reporting, second number sets period (dependant on datarate)
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set TX power
ser.write(b"AT+CTXP=0\r\n")#0 = 17dBm
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#Set linkcheck
ser.write(b"AT+CLINKCHECK=2\r\n")#0 = disable, 1 = one time, 2 each time check link after sending data
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#enable ADR
ser.write(b"AT+CADR=1\r\n")#0 = disable, 1 = enable ADR (adaptive data rate) function
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#set RX-window parameter
ser.write(b"AT+CRXP=0,0,869525000\r\n")#first nr = offset left, second nr = offset right, third nr = frequency
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#set receive delay
ser.write(b"AT+CRX1DELAY=2\r\n")#decimal number for amount of seconds to hold receive window open
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#save all parameters
ser.write(b"AT+CSAVE\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return: "OK"

#send a testframe of data
ser.write(b"AT+DTRX=1,2,10,0123456789\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))
#this should return:
#"OK+SEND:03"
#"OK+SENT:01"
#"OK+RECV:02,01,00"

ser.write(b"AT+DRX?\r\n")
time.sleep(0.1)
print(wait_response(ser, 7))

ser.close()
