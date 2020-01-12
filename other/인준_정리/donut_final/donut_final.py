import matplotlib.pyplot as plt
import matplotlib.animation as animation
from socket import *
import time
port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.43.191', port))

print('접속 완료')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), subplot_kw=dict(aspect="equal"))

def making_graph(ax, quantity,color1,color2,fruit):
    color = [color1,color2]
    data = [int(quantity), 100-int(quantity)]

    wedges, texts = ax.pie(

                            data,## data function
                            wedgeprops=dict(width=0.1),##wedge 두께
                            startangle=90,##시작 동경(90도 위치)
                            counterclock=False,##시계방향
                            colors=color,##색깔 array
                            radius=1.2,##반지름
                            ##center=(100,31),##그래프 위치(근데 작동안됨)

                           )
    ax.text(-1,-0.05,s=fruit,fontsize=20, fontweight='bold',)

def animate(i):
    time.sleep(1.5)
    recvData = clientSock.recv(1024)
    tprocData = recvData.decode('utf-8')
    procData = tprocData.split('||')

    #procData = '25/40/60/75'
    amount_of_fruit = procData[0].split('/')
    print(amount_of_fruit)

    if len(amount_of_fruit) > 2:

        making_graph(ax1,amount_of_fruit[0],'#fc4a85','#ffe0ea','Strawberry')
        making_graph(ax2,amount_of_fruit[1],'#fcec60','#fffbcf','Banana')
        making_graph(ax3,amount_of_fruit[2],'#b561ff','#e3c2ff','Grape')
        making_graph(ax4,amount_of_fruit[3],'#4aff26','#ceffc4','Apple')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
