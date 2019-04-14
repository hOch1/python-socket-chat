from socket import *
from select import *
import sys
from time import ctime

HOST = '127.0.0.1'
PORT = 10001
BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket(AF_INET, SOCK_STREAM) #소켓생성

clientSocket.connect(ADDR) #서버에 접속

while True:
    line = input()
    clientSocket.sendall(line.encode()) #문자 전송
    if not line: break # line이 비어있을경우 통신 종료
    data = clientSocket.recv(65534) # 서버측 data 수신
    print(data.decode())
clientSocket.close()
