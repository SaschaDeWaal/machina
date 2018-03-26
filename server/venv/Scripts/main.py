import socket
import thread
from RobotConnection import RobotConnection;

def onNewClient(clientsocket, addr):
    robotConnection = RobotConnection(clientsocket, addr);

sock = socket.socket()
host = socket.gethostname()
port = 12345;
sock.bind((host, port))

print "server runnging, waiting on connection";

sock.listen(5)

while True:
   c, addr = sock.accept()
   thread.start_new_thread(onNewClient, (c, addr))

sock.close()