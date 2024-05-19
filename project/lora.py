#!usr/bin/python3
import serial
import time
from send_data import *

ser = open_serial()

def send_command(command):
    time.sleep(0.1)
    ser.write(("AT+" + command + "\r\n").encode())
    

ser.write(b"AT\r\n")
time.sleep(0.1)
print(wait_response(ser, 1))

#restore all settings to factory defaults if something goes wrong
#send_command("CRESTORE")
#this should return: "OK"
 
#set Join Mode to OTAA (Over The Air Activation)
send_command("CJOINMODE=0")
print(wait_response(ser, 1))
#this should return: "OK"

#manually set DEVEUI to what the Digita network expects
send_command("CDEVEUI=05B18B2C5428A0DA")
print(wait_response(ser, 1))
#This should return: "OK"

#manually set APPEUI (now JOINEUI) to what Digita network expects
send_command("CAPPEUI=0000000000000000")
print(wait_response(ser, 1))
#This should return: "OK"

#manually set APPKEY to what Digita network expects
send_command("CAPPKEY=528370A16B76AD2475E1BA621DAA5BCC") #32 byte address
print(wait_response(ser, 1))
#This should return: "OK"

#manually set APPKEY to what Digita network expects
send_command("CDEVADDR=5428A0DA") #16 byte address
print(wait_response(ser, 1))
#This should return: "OK"

#manually set frequency band mask
send_command("CFREQBANDMASK=0001") #4 byte address
print(wait_response(ser, 1))
#This should return: "OK"

#manually set upload/downloadmode on different frequencies
send_command("CULDLMODE=2") #1 = same, 2 = different frequency
print(wait_response(ser, 1))
#This should return: "OK"

#manually set the workmode to "Normal"
send_command("CWORKMODE=2") #only this option is supported
print(wait_response(ser, 1))
#This should return: "OK"


#for lowest energy consumption we will use this device as a class A
send_command("CCLASS=0") #0 = CLASS A, 1 = CLASS B, 2 = CLASS C
print(wait_response(ser, 1))
#This should return: "OK"

#get battery level
send_command("CBL?")
print(wait_response(ser, 1))
#this should return: "+CBL:x" with x = battery percentage
#if no battery is present this will return: "CBL:100"

send_command("CSTATUS?")
print(wait_response(ser, 1))
#status response overview
#00 = no data operation
#01 = data sending
#02 = data sending failed
#03 = data sending success
#04 join succes
#05 join fail
#06 network may abnormal (res from Link Check)
#07 data sent success, no download
#08 data sent success, yes download

#Try to join the network with OTAA
send_command("CJOIN=1,1,8,10")
print(wait_response(ser, 1))
#this should return: "OK"

#Set up for uplink confirmation for messaging:
send_command("CCONFIRM=0") #1 =confirm, 0 = unconfirm uplink message
print(wait_response(ser, 1))
#this should return: "OK"

#Set up application port
send_command("CAPPPORT=5") #decimal number in [1:223], 0x00 is reserved for LoRaWAN MAC command
print(wait_response(ser, 1))
#this should return: "OK"

#Set up spreading factor and datarate
#send_command("CDATARATE=4") #decimal number in [0:5], higher number = lower SF
#this should return: "OK"

#inquire RSSI
send_command("CRSSI FREQBANDIDX?")
print(wait_response(ser, 1))
#this should return a list x:<RSSI value> with x decimal number in [0:7]
#this lists the RSSI for all the frequency channels set previously with command "CFREQBANDMASK"

#Set number of trials for sending data
send_command("CNBTRIALS=0,1") #first number 1 = confirm, 0 = uncomfirm package, second number in range [1:15] sets number of trials
print(wait_response(ser, 1))
#this should return: "OK"

#Set report mode
#send_command("CTXP=0,0")#first number 0 = non periodic, 1 = periodic data reporting, second number sets period (dependant on datarate)
#this should return: "OK"

#Set TX power
#send_command("CTXP=0")#0 = 17dBm
#this should return: "OK"

#Set linkcheck
send_command("CLINKCHECK=1")#0 = disable, 1 = one time, 2 each time check link after sending data
print(wait_response(ser, 1))
#this should return: "OK"

#enable ADR
send_command("CADR=0")#0 = disable, 1 = enable ADR (adaptive data rate) function
print(wait_response(ser, 1))
#this should return: "OK"

#set RX-window parameter
#send_command("CRXP=0,0,869525000")#first nr = offset left, second nr = offset right, third nr = frequency
#this should return: "OK"

#set receive delay
#send_command("CRX1DELAY=0")#decimal number for amount of seconds to hold receive window open
#this should return: "OK"

#save all parameters
send_command("CSAVE")
print(wait_response(ser, 1))
#this should return: "OK"

""" code for testing
#send a testframe of data
send_command("DTRX=0,0,10,0123456789")
print(wait_response(ser, 1))
#this should return:
#"OK+SEND:03"
#"OK+SENT:01"
#"OK+RECV:02,01,00"

#check for new data
send_command("DRX?")
print(wait_response(ser, 1))
ser.close()
"""
