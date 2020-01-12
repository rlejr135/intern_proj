import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from socket import *


port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')
plt.ion()

'''
def making_graph1():

    recipe = ["225 g flour",
              "90 g sugar",
              "1 egg",
              "60 g butter",
              "100 ml milk",
              "1/2 package of yeast"]

    #data = [recvData.decode('utf-8'), 90, 50, 60, 100, 5]
    data = [225, 90, 50, 60, 100, 5]

    wedges, texts = ax1.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax1.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
'''
def making_graph(ax, quantity,color1,color2):
    color = [color1,color2]
    data = [int(quantity), 100-int(quantity)]
    #data = [225, 90]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=90, colors=color)


while True:

    recvData = clientSock.recv(1024)
    procData = recvData.decode('utf-8')
    amount_of_fruit = procData.split('/')
    plt.close()
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    making_graph(ax1,amount_of_fruit[0],'red','lightsalmon')
    making_graph(ax2,amount_of_fruit[1],'gold','lemonchiffon')
    making_graph(ax3,amount_of_fruit[2],'m','violet')
    making_graph(ax4,amount_of_fruit[3],'lime','greenyellow')


    plt.pause(2)
'''
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(6, 3), subplot_kw=dict(aspect="equal"))

making_graph(ax1,12,'red','lightsalmon')
making_graph(ax2,46,'gold','lemonchiffon')
making_graph(ax3,25,'m','violet')
making_graph(ax4,36,'lime','greenyellow')
plt.show()
'''
