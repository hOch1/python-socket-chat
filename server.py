from socket import *
from select import *

HOST = ''
PORT = 10001
BUFSIZE = 1024
ADDR = (HOST, PORT)

#소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

#소켓 주소
serverSocket.bind(ADDR)

#연결 수신
serverSocket.listen(1)

#연결 수락
clientSocekt, addr_info = serverSocket.accept()
print(clientSocekt)

while True:
    data = clientSocekt.recv(65535)
    if not data : break # 받은 data가 없을시에 통신종료
    print(data.decode()) # 받은 data출력
    line = input()
    clientSocekt.sendall(line.encode()) # 문자 전송

clientSocekt.close()
