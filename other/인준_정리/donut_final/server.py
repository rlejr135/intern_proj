from socket import *


port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

a = 20
b = 40
c = 60
d = 80

while True:
    sendData = str(a) + '/' + str(b)
    a = a + 1
    b = b + 1
    c = c + 1
    d = d + 1
    if a > 100:
        a = 0
    if b > 100:
        b = 0
    if c > 100:
        c = 0
    if d > 100:
        d = 0
    connectionSock.send(sendData.encode('utf-8'))
