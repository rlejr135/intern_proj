#!usr/bin/env python
# -*- coding: utf-8 -*-



import sys, os
import sys, time, http.client
from urllib.request import urlopen
import requests
import webbrowser

HOST = '127.0.0.1'  # insert web app's address
PORT = '8000'

BASE_URL = "http://" + HOST + ':' + PORT + '/'

#BASE_URL = "http://asmryealim9702.pythonanywhere.com/"

Debug = False

def connection_ok():
    global BASE_URL
    cmd = 'ConnectionTest'
    url = BASE_URL + cmd
    print('url: %s'% url)
    # if server find there is 'connection_test' in request url, server will response 'Ok'
    try:
        r=requests.get(url)
        if r.text == 'OK':
            return True
    except:
        return False

def __request__(url,times = 10):
    for x in range(times):
        try:
            r = requests.get(url)
            print('received url : %s'%url)
            print (r.text)
            return 0
        except:
            print("connection error!")
        print("abort!")


def send_data(data):
    global BASE_URL
    ddata = {}

    ddata[str(data)] = 1


    requests.get(BASE_URL + 'run/', params=ddata)


def connection_start(save_data):
    global BASE_URL

    if connection_ok() == True:
        print("connection complete")
        #for k in save_data:
        send_data(save_data)


        webbrowser.open_new_tab(BASE_URL + 'post/')
    else:
        print("connection failed")



# for test connection

if Debug == True:
    data = [
        {'title': '캐릭터 라이선싱 페어 2019', 'start': '2019.07.17', 'finish': '2019.07.21', 'number': '02-6000-8570~1', 'address': '서울특별시 강남구 영동대로 513', 'img': 'https://support.visitkorea.or.kr/img/call?cmd=VIEW&id=c6ec3ad0-a2da-44ff-a3d0-f8f70fdc8c46'}
    ]
    connection_start(data)
