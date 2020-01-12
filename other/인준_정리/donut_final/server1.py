import socket
import time

port = 8080

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('', port))
ss.listen(1)

print('%d번 포트로 접속 대기중...'%port)


connectionSock, address = ss.accept()

print(str(address), '에서 접속되었습니다.')


a=80
b=70
c=70
d=12

while True:


    sendData = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d)

    time.sleep(1)
    a=a+1
    b=b+1
    c=c+1
    d=d-1



    connectionSock.send(sendData.encode('utf-8'))
