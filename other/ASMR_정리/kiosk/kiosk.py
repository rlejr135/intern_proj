import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import signal
from PyQt5 import uic
import time
import csv
import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from datetime import datetime


CalUI = 'kiosk.ui'
tmp_amount_data = 0
juice_name = '주스'
tmp_fruit_data_1 = 0
tmp_fruit_data_2 = 0

saved_data_time = []
save_content = {}
data = {}
data1 = {}

save_data_sell = {"딸기" : 0, "딸기바나나" : 0 , "딸기블루베리" : 0, "딸기수박" : 0, "바나나블루베리" : 0, "바나나" : 0, "바나나수박" : 0, "블루베리" : 0, "수박블루베리" : 0 , "수박" : 0}
'''''
for each customer:
    save_content['시간'] = time
    save_content['fruit id'] = banana

    saved_data_time.append(save_content)

for each customer:
    save_data_sell['딸바'] += 1
'''


class MainDialog(QDialog):

    def __init__(self):

        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.strawberry.clicked.connect(self.strawberry_event)
        self.banana.clicked.connect(self.banana_event)
        self.blueberry.clicked.connect(self.blueberry_event)
        self.watermelon.clicked.connect(self.watermelon_event)
        self.strawberry_2.clicked.connect(self.strawberry_event_2)
        self.banana_2.clicked.connect(self.banana_event_2)
        self.blueberry_2.clicked.connect(self.blueberry_event_2)
        self.watermelon_2.clicked.connect(self.watermelon_event_2)
        self.apply.clicked.connect(self.apply_event)
        self.end_button.clicked.connect(self.end_event)


        self.strawberry.setStyleSheet(  # "color: green;"
         "border:5px solid rgba(0, 0, 0,0%);"
         #"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0);" #fff, stop: 1 #888
            'image : url(kiosk_image/strawberry.jpg)')
        self.banana.setStyleSheet(  # "color: green;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/banana.jpg)')
        self.blueberry.setStyleSheet(  # "color: blue;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/blueberry.jpg)')
        self.watermelon.setStyleSheet(  # "color: blue;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/watermelon.jpg)')

        self.strawberry_2.setStyleSheet(  # "color: red;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image : url(kiosk_image/strawberry.jpg)')
        self.banana_2.setStyleSheet(  # "color: green;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/banana.jpg)')
        self.blueberry_2.setStyleSheet(  # "color: blue;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/blueberry.jpg)')
        self.watermelon_2.setStyleSheet(  # "color: blue;"
         "border:5px solid rgba(0, 0, 0,0%);"
            'image:url(kiosk_image/watermelon.jpg)')
        self.background.setStyleSheet(  # "color: blue;"
            #'background-color: rgba(0,0,0,0%);'
            'image:url(kiosk_image/1.png)')




    def strawberry_event(self):
        global tmp_fruit_data_1
        print('Click!!!!1')
        tmp_fruit_data_1 = 1
        print(tmp_fruit_data_1)
        self.strawberry.setStyleSheet("border-color: rgb(255, 0, 0);"
             "border:10px solid rgb(89, 45, 0);"
            'image : url(kiosk_image/strawberry.jpg)')



    def banana_event(self):
        global tmp_fruit_data_1
        print('Click!!!!1')
        tmp_fruit_data_1 = 2
        print( tmp_fruit_data_1)
        self.banana.setStyleSheet("border-color: rgb(255, 0, 0);"
                                      "border:10px solid rgb(89, 45, 0);"
                                      'image : url(kiosk_image/banana.jpg)')

    def watermelon_event(self):
        global  tmp_fruit_data_1
        print('Click!!!!1')
        tmp_fruit_data_1 = 3
        print( tmp_fruit_data_1)
        self.watermelon.setStyleSheet("border-color: rgb(255, 0, 0);"
                                  "border:10px solid rgb(89, 45, 0);"
                                  'image : url(kiosk_image/watermelon.jpg)')

    def blueberry_event(self):
        global  tmp_fruit_data_1
        print('Click!!!!1')
        tmp_fruit_data_1 = 4
        print( tmp_fruit_data_1)
        self.blueberry.setStyleSheet("border-color: rgb(255, 0, 0);"
                                  "border:10px solid rgb(89, 45, 0);"
                                  'image : url(kiosk_image/blueberry.jpg)')

    def strawberry_event_2(self):
        global tmp_fruit_data_2
        print('Click!!!!1')
        tmp_fruit_data_2 = 1
        print( tmp_fruit_data_2)
        self.strawberry_2.setStyleSheet("border-color: rgb(255, 0, 0);"
                                      "border:10px solid rgb(89, 45, 0);"
                                      'image : url(kiosk_image/strawberry.jpg)')

    def banana_event_2(self):
        global tmp_fruit_data_2
        print('Click!!!!1')
        tmp_fruit_data_2 = 2
        print(tmp_fruit_data_2)
        self.banana_2.setStyleSheet("border-color: rgb(255, 0, 0);"
                                        "border:10px solid rgb(89, 45, 0);"
                                        'image : url(kiosk_image/banana.jpg)')

    def watermelon_event_2(self):
        global tmp_fruit_data_2
        print('Click!!!!1')
        tmp_fruit_data_2 = 3
        print(tmp_fruit_data_2)
        self.watermelon_2.setStyleSheet("border-color: rgb(255, 0, 0);"
                                    "border:10px solid rgb(89, 45, 0);"
                                    'image : url(kiosk_image/watermelon.jpg)')

    def blueberry_event_2(self):
        global tmp_fruit_data_2
        print('Click!!!!1')
        tmp_fruit_data_2 = 4
        print(tmp_fruit_data_2)
        self.blueberry_2.setStyleSheet("border-color: rgb(255, 0, 0);"
                                    "border:10px solid rgb(89, 45, 0);"
                                    'image : url(kiosk_image/blueberry.jpg)')

    def apply_event(self):
        global tmp_amount_data
        global juice_name
        global fruit

        tmp_amount_data = tmp_amount_data + 1
        if tmp_fruit_data_1 == 1 and tmp_fruit_data_2 == 1:
            juice_name = '딸기'
            save_data_sell['딸기'] += 1


        elif (tmp_fruit_data_1 == 1 and tmp_fruit_data_2 == 2) or (tmp_fruit_data_1 == 2 and tmp_fruit_data_2 == 1):
            juice_name = '딸기바나나'
            save_data_sell['딸기바나나'] += 1


        elif (tmp_fruit_data_1 == 1 and tmp_fruit_data_2 == 3) or (tmp_fruit_data_1 == 3 and tmp_fruit_data_2 == 1):
            juice_name = '딸기수박'
            save_data_sell['딸기수박'] += 1

        elif (tmp_fruit_data_1 == 1 and tmp_fruit_data_2 == 4) or (tmp_fruit_data_1 == 4 and tmp_fruit_data_2 == 1):
            juice_name = '딸기블루베리'
            save_data_sell['딸기블루베리'] += 1

        elif (tmp_fruit_data_1 == 2 and tmp_fruit_data_2 == 2) :
            juice_name = '바나나'
            save_data_sell['바나나'] += 1

        elif (tmp_fruit_data_1 == 2 and tmp_fruit_data_2 == 3) or (tmp_fruit_data_1 == 3 and tmp_fruit_data_2 == 2) :
            juice_name = '바나나수박'
            save_data_sell['바나나수박'] += 1

        elif (tmp_fruit_data_1 == 2 and tmp_fruit_data_2 == 4) or (tmp_fruit_data_1 == 4 and tmp_fruit_data_2 == 2):
            juice_name = '바나나블루베리'
            save_data_sell['바나나블루베리'] += 1

        elif tmp_fruit_data_1 == 3 and tmp_fruit_data_2 == 3:
            juice_name = '수박'
            save_data_sell['수박'] += 1

        elif (tmp_fruit_data_1 == 3 and tmp_fruit_data_2 == 4) or (tmp_fruit_data_1 == 4 and tmp_fruit_data_2 == 3):
            juice_name = '수박블루베리'
            save_data_sell['수박블루베리'] += 1

        elif tmp_fruit_data_1 == 4 and tmp_fruit_data_2 == 4:
            juice_name = '블루베리'
            save_data_sell['블루베리'] += 1




        QMessageBox.about(self, "message", juice_name + " 주스 주문이 완료되었습니다")


        self.strawberry.setStyleSheet(  # "color: green;"
             "border:5px solid rgba(0, 0, 0,0%);"
             "border-radius: 20px;"
                'image : url(kiosk_image/strawberry.jpg)')
        self.banana.setStyleSheet(  # "color: green;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/banana.jpg)')
        self.blueberry.setStyleSheet(  # "color: blue;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/blueberry.jpg)')
        self.watermelon.setStyleSheet(  # "color: blue;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/watermelon.jpg)')

        self.strawberry_2.setStyleSheet(  # "color: red;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image : url(kiosk_image/strawberry.jpg)')
        self.banana_2.setStyleSheet(  # "color: green;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/banana.jpg)')
        self.blueberry_2.setStyleSheet(  # "color: blue;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/blueberry.jpg)')
        self.watermelon_2.setStyleSheet(  # "color: blue;"
             "border:5px solid rgba(0, 0, 0,0%);"
                'image:url(kiosk_image/watermelon.jpg)')


    def end_event(self):
        global tmp_amount_data
        global data
        print(tmp_amount_data)
        print(save_data_sell)

        QMessageBox.about(self, "message", "오늘 총 판매량은 "+ str(tmp_amount_data) + "잔 입니다.")
        #QMessageBox.setStyleSheet("QLabel{min-width:500 px; font-size: 24px;} QPushButton{ width:250px; font-size: 18px; }");

        self.close()

        johap = []

        for keys in save_data_sell.keys():
            johap.append(keys)

        sell = []

        for value in johap:
            sell.append(save_data_sell[value])

        print(johap)
        print(sell)

        foods = []

        #딸기
        foods.append(sell[0]*5 + sell[1]*3 + sell[2]*3 + sell[3]*3)
        #바나나
        foods.append(sell[1]*3 + sell[4]*5 + sell[5]*3 + sell[6]*3)
        #수박
        foods.append(sell[3]*3 + sell[6]*3 + sell[8]*3 + sell[9]*5)
        #블루베리
        foods.append(sell[2]*3 + sell[4]*3 + sell[7]*5 + sell[8]*3)

        print(foods)

        '''
        f = open('output.csv', 'a')

        #f.write("Date,Low_temp,High_temp,Rainfall,Humidity,Region,IsHoliday,Strawberry,Banana,Watermelon,Blueberry\n")

        #f.write(data[1]+','+ data[0]+','+data[3]+','+data[2]+','+'1'+','+'False')
        f.write(data[1])




        f.close()
        '''
        df = pd.read_csv("./output.csv", engine='python') #csv 파일 뽑기

        colors = ['lightslategray', ] * 10
        colors[0] = 'rgb(65,3,157)'
        colors[1] = 'rgb(111,1,167)'
        colors[2] = 'rgb(137,13,162)'
        colors[3] = 'rgb(160,27,155)'
        colors[4] = 'rgb(192,59,131)'
        colors[5] = 'rgb(222,97,100)'
        colors[6] = 'rgb(239,126,80)'
        colors[7] = 'rgb(250,157,59)'
        colors[8] = 'rgb(252,179,49)'
        colors[9] = 'rgb(249,218,36)'

        # Add table data

        now = QDate.currentDate()
        now2= datetime.now( ) #날짜]
        today = str(now2.year)+"-"+str(now2.month)+"-"+str(now2.day)

        print(now.toString(Qt.DefaultLocaleLongDate))

        f = open("weather_day_text.txt", "r")
        i=0
        while True:
            line = f.readline()
            if not line: break
            data1[i] = line
            data[i] = data1[i].replace("\n","")
            i=i+1
            print(line)

        print(data)

        table_data = [['Data','Value' ],
                      ['<b>날짜', now.toString(Qt.ISODate)],
                      ['<b>장소', '서울시 성동구'],
                      ['<b>최고기온', data[0]+'°C'],
                      ['<b>최저기온', data[1]+'°C'],
                      ['<b>습도', data[2]+'%'],
                      ['<b>강수량', data[3] + 'mm']]

        f = open('output.csv', 'a')
        f.write(today+','+str(data[1])+','+ str(data[0])+','+str(data[3])+','+data[2]+',1,False,'+str(foods[0])+','+str(foods[1])+','+str(foods[2])+','+str(foods[3])+'\n')
        f.close()



        food_colors = ['rgb(255, 113, 113)', 'rgb(255, 250, 138)', 'rgb(157, 255, 157)',
                        'rgb(224, 147, 253)']
        #table1 = ff.create_table(table_data, height_constant=60)

        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{"type": "table"}, {'type':'domain'}],
                   [{"colspan": 2}, None]],
            subplot_titles=("","<b>식재료 판매비율", "<b>메뉴별 판매량"))

        #fig = ff.create_table(table_data, height_constant=60)
        #fig.add_trace(table1.data[0], 1, 1)
        fig.add_trace(
            go.Table(
                header=dict(
                    values=["<b>Data", "<b>Values"],
                    font=dict(size=20),
                    align="center",
                    height= 50
                ),
                cells=dict(
                    values=[
                      ['<b>장소','<b>최고기온','<b>최저기온','<b>습도','<b>강수량'],
                    ['서울시 성동구', data[0]+'°C',data[1]+'°C',data[2]+'%',data[3] + 'mm']],
                    font=dict(size=20),
                    align="center",
                    height=50
                )
            ),
            row=1, col=1
        )

        fig.add_trace(go.Pie(labels=['딸기','바나나','수박','블루베리'], values=foods,hole=.3,marker_colors=food_colors,textinfo='label+percent'),
                      row=1, col=2)

        fig.add_trace(go.Bar(x=johap, y=sell, xaxis='x2', yaxis='y2',showlegend =False,
                             marker=dict(color=colors)),
                      row=2, col=1)


        fig.update_layout(showlegend=False, title_text= now.toString(Qt.DefaultLocaleLongDate) + ' <b>판매 정보', title_font_size =53,font_size=15,)
        fig.layout.update({'height': 1200},margin=dict(l=20, r=20, t=350, b=20))
        fig.show()
        '''
        # Initialize a figure with ff.create_table(table_data)
        fig = ff.create_table(table_data, height_constant=60)


        # Make traces for graph
        trace1 = go.Bar(x=johap, y=sell, xaxis='x2', yaxis='y2',
                        marker=dict(color=colors),
                        name='판매량 For<br>Per Game')

        fig.add_trace(go.Pie(values=[2,1,3]))


        # Add trace data to figure
        fig.add_traces([trace1])

        # initialize xaxis2 and yaxis2
        fig['layout']['xaxis2'] = {}
        fig['layout']['yaxis2'] = {}
        fig['layout']['xaxis3'] = {}
        fig['layout']['yaxis3'] = {}

        # Edit layout for subplots
        fig.layout.xaxis.update({'domain': [0, .25]})
        fig.layout.xaxis2.update({'domain': [0.35, 0.98]})


        #fig.layout.yaxis.update({'domain': [0, .45]})
        #fig.layout.yaxis2.update({'domain': [.6, 1]})

        # The graph's yaxis2 MUST BE anchored to the graph's xaxis2 '
        # BNMM<NMN
        fig.layout.yaxis2.update({'anchor': 'x2'})
        fig.layout.xaxis2.update({'anchor': 'y2'})
        fig.layout.yaxis2.update({'title': dict(text = '<b>Sales', font_size = 15)})

        # Update the margins to add a title and see graph x-labels.
        fig.layout.margin.update({'t': 80, 'l': 50})
        fig.layout.update({'title': dict(text = now.toString(Qt.DefaultLocaleLongDate) + ' <b>판매 정보', font_size=30)})
        #fig.layout.update({'font': dict(family='타이포_쌍문동 B', size=15, color='#7f7f7f')})



        # Update the height because adding a graph vertically will interact with
        # the plot height calculated for the table
        fig.layout.update({'height': 550})

        # Plot!
        fig.show()

        #fig = px.bar(df, x='menu', y='sales', marker_color='crimson', name ='menu')

        #fig = px.bar(df, x='menu', y='sales', marker_color=colors)
        #fig = go.Figure(data=[go.Bar(x=johap, y=sell, marker_color = colors)])
        #fig.updata_yaxes(dtick=1)
        #fig.show()

'''
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
