import serial
import sys
import string

print "start";

ser = serial.Serial(port='/dev/ttyS0', baudrate = 115200)

while True:
    try:
        # Read data incoming on the serial line
        data = ser.readline()
        print data
    except:
        print "Unexpected error:", sys.exc_info()
        sys.exit()