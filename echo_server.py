from socket import *
from time import ctime
def srvSocket():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpSrvSock = socket(AF_INET, SOCK_STREAM)
    tcpSrvSock.bind(ADDR)
    tcpSrvSock.listen(5)

    while True:
        print ('Wating for Connection...')
        tcpCliSock, address = tcpSrvSock.accept()

        print('Connection from :', address)

        while True:
            recvData = tcpCliSock.recv(BUFSIZE)
            if not recvData:
                print('no DATA')
                break
            tcpCliSock.send(('[%s] %s'%(ctime(), recvData)).encode('utf-8'))
        tcpCliSock.close()

    tcpSrvSock.close()

if __name__ == '__main__':
    srvSocket()
