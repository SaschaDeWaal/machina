import time
import thread
import socket

class NetworkManager:

    def __init__(self):
        self.socket = socket.socket()
        self.host = '10.3.21.242'
        self.port = 12345;
        self.connected = False

    def startConnection(self):
        self.socket.connect((self.host, self.port))
        self.connected = True

        while True:
            msg = clientsocket.recv(1024)
            self.onMessage(msg)

    def onMessage(self, msg):
        print msg

    def sendMessage(self, msg):
        if self.connected:
            self.socket.sendall(msg)

    def closeConnection(self):
        self.socket.close()
