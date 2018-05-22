from threading import Thread
import serial
import sys
import json

class ArduinoBridge:
    """ This class is the bridge between the arduino and the raspberry pi.
    You can use it to send commands to the Arduino and get the latest sensor data from the arduino """

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=5)
        self.lastData = json.loads('{}')

        self.open = True
        self.thread = Thread(target=self.arduinoConnection, args=())
        self.thread.start()

    def arduinoConnection(self):
        print "start connection to arduino"
        while self.open:
            data = self.ser.readline()
            try:
                if data[0] == "{":
                    self.lastData = json.loads(data)
                    print(data)
            except:
                print "Unexpected error:", sys.exc_info()
                sys.exit()

    def send(self, msg):
        """ Send a command to the arduino """
        if self.open:
            self.ser.write((msg + ";").encode())

    def stop(self):
        """ Close the serial connection to the arduino """
        self.open = False
        self.ser.close()
