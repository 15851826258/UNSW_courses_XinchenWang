import sys
from socket import *

server_port = int(sys.argv[1])  # get the port from input

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)
# the server is ready to receive

while 1:
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == "":
            continue
        # print(f"\n request result is :")
        # print(sentence)
        filename = sentence.split()[1][1:]  # get the filename
        # There is a '/'before the file name use [1:] to remove it
        file_ob = open(filename, 'rb')  # rb means that read in binary mode
        file_content = file_ob.read()
        # print(file_content)
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        connectionSocket.send(file_content)
    except:
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send(b"404 Not Found")

    connectionSocket.close()

# python WebServer.py 90 fro test
# code by Louis xinchen wang z5197409
