from socket import *
from sqlite3 import connect
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is listening on", serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        
        response = 'HTTP/1.0 200 OK\n\n'
        connectionSocket.send(response.encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())        
        connectionSocket.close()
    except IOError:
        response = 'HTTP/1.0 404 Not Found\n\nFile Not Found'
        connectionSocket.sendall(response.encode())
        connectionSocket.close()
        print("error")

serverSocket.close()
sys.exit()