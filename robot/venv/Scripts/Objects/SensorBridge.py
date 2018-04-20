from threading import Thread
import serial
import sys
import json

class SensorBridge:

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate = 115200, timeout = 5)
        self.lastData = json.loads('{}')

        self.listening = True
        self.thread = Thread(target=self.arduinoConnection, args=())
        self.thread.start()

    def arduinoConnection(self):
        while self.listening:
            try:
                data = self.ser.readline()
                self.lastData = json.loads(data)
            except:
                print "Unexpected error:", sys.exc_info()
                sys.exit()

    def stop(self):
        self.listening = False
        self.ser.close();