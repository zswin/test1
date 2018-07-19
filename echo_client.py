from socket import *

def clientSocket():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data = str(input('please input:'))
        print(data)
        if not data:
            break
        tcpCliSock.send(data.encode('utf-8'))
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print(data)

    tcpCliSock.close()

if __name__ == '__main__':
    clientSocket()

