import socket

class RobotConnection:

    def __init__(self, clientsocket, addr):
        self.clientsocket = clientsocket;
        self.addr = addr;
        print 'open connection from ', addr

        while True:
            msg = clientsocket.recv(1024)
            self.onMessage(msg)

        self.closeConnection()

    def onMessage(self, msg):
        print msg

    def sendMessage(self, msg):
        self.clientsocket.sendall(msg)

    def closeConnection(self):
        self.clientsocket.close()