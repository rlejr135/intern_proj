import matplotlib.pyplot as plt
import matplotlib.animation as animation
from socket import *
import time
port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.43.191', port))

print('접속 완료')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), subplot_kw=dict(aspect="equal"))

def making_graph(ax, quantity,color1,color2):
    color = [color1,color2]
    data = [int(quantity), 100-int(quantity)]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=90, colors=color)

def animate(i):
    time.sleep(1.5)
    recvData = clientSock.recv(1024)
    tprocData = recvData.decode('utf-8')
    procData = tprocData.split('||')
    amount_of_fruit = procData[0].split('/')
    print(amount_of_fruit)

    if len(amount_of_fruit) > 2:

        making_graph(ax1,int(amount_of_fruit[0]),'red','lightsalmon')
        making_graph(ax2,int(amount_of_fruit[1]),'gold','lemonchiffon')
        making_graph(ax3,int(amount_of_fruit[2]),'m','violet')
        making_graph(ax4,int(amount_of_fruit[3]),'lime','greenyellow')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
