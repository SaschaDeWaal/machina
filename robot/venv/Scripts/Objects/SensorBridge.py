from threading import Thread
import serial
import sys
import json

class SensorBridge:

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate = 9600, timeout = 5)
        self.lastData = json.loads('{}')

        self.listening = True
        self.thread = Thread(target=self.arduinoConnection, args=())
        self.thread.start()

    def arduinoConnection(self):
        print "start  to arduino"
        while self.listening:
            data = self.ser.readline()
            try:
                if data[0] == "{":
                    self.lastData = json.loads(data)
                    print(data)
            except:
                print "Unexpected error:", sys.exc_info()
                sys.exit()

    def send(self, msg):
        self.ser.write((msg + ";").encode())


    def stop(self):
        self.listening = False
        self.ser.close()
