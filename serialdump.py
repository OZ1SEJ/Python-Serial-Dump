#!/usr/bin/python3.6
import serial

ser = serial.Serial('/dev/ttyACM2',9600)
f   = open("serialdump.txt", "a+")


while True:
    s    = ser.readline()
    line = s.decode('utf-8').replace('\r\n','')
    print(line)		# Prints output to screen
    f.write(line)	# Appends output to file
