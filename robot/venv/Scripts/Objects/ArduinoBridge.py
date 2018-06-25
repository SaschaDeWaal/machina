from threading import Thread
import serial
import sys
import json
import time
import RPi.GPIO as GPIO

class ArduinoBridge:
    """ This class is the bridge between the arduino and the raspberry pi.
    You can use it to send commands to the Arduino and get the latest sensor data from the arduino """

    def __init__(self):
        """
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=5)
        self.lastData = json.loads('{"index":"1286","gyroscoop":[-90.00,90.00,-0.00],"accelerator":[-0.00,-0.00,-0.00],"temperature":"-76.33","battery":"1024","light":[240,238,238]}')

        self.open = True
        self.thread = Thread(target=self.arduinoConnection, args=())
        self.thread.start()
        """
        print "Open connection to arduino"
		
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=5)
        self.lastData = json.loads('{"index":"0","gyroscoop":[0,0,0],"accelerator":[0,0,0],"temperature":"0","battery":"1024","light":[false,false,false]}')
		
		print "Reset arduino"
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12, GPIO.OUT)
		GPIO.output(12, False)
		time.sleep(0.5)
		GPIO.output(12, True)
		time.sleep(1)
		
        print "Waiting on first msg from the arduino (arduino needs to calibrate the sensors first)"
		
		arduinoIsDone = False
		while(arduinoIsDone == False):
			data = self.ser.readline()
			try:
				if data[0] == "{":
					self.lastData = json.loads(data)
					arduinoIsDone = True
			except:
				pass
			
		print "Connection is open"
		
		self.open = True
		self.thread = Thread(target=self.arduinoConnection, args=())
		self.thread.start()
		

    def arduinoConnection(self):
        while self.open:
            try:
                data = self.ser.readline()
                print "receive from arduino: " + data
                if data[0] == "{":
                    self.lastData = json.loads(data)
            except:
                pass

    def send(self, msg):
        """ Send a command to the arduino """
        if self.open:
            self.ser.write(msg)

    def stop(self):
        """ Close the serial connection to the arduino """
        self.open = False
        self.ser.close()

    def setTeamColour(self, number):
        if number == 0:
            self.send('set color 1')
        if number == 1:
            self.send('set color 2')
        if number == 2:
            self.send('set color 3')
