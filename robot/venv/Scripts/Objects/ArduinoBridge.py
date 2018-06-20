from threading import Thread
import serial
import sys
import json

class ArduinoBridge:
    """ This class is the bridge between the arduino and the raspberry pi.
    You can use it to send commands to the Arduino and get the latest sensor data from the arduino """

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=5)
        self.lastData = json.loads('{"index":"1286","gyroscoop":[-90.00,90.00,-0.00],"accelerator":[-0.00,-0.00,-0.00],"temperature":"-76.33","battery":"1024","light":[240,238,238]}')

        self.open = True
        self.thread = Thread(target=self.arduinoConnection, args=())
        self.thread.start()

    def arduinoConnection(self):
        print "start connection to arduino"
        while self.open:
            data = self.ser.readline()
            print "baconeggsandcheeseontoastwithsriracha"
            print(data)
            try:
                if data[0] == "{":
                    self.lastData = json.loads(data)
                    print "LASTDATA:"
                    print self.lastData
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
            self.send('1')
        if number == 1:
            self.send('2')
        if number == 2:
            self.send('3')
