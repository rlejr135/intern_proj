import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import signal
from PyQt5 import uic
import choice

CalUI = 'gui_2.ui'

tmp_option_data = 0
tmp_region_data = 0

class MainDialog(QDialog):

    def __init__(self):
        global tmp_option_data
        global tmp_region_data
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.pushButton_1.clicked.connect(self.OptionClicked_1)
        self.pushButton_2.clicked.connect(self.OptionClicked_2)
        self.pushButton_3.clicked.connect(self.OptionClicked_3)
        self.pushButton_4.clicked.connect(self.applyButton)

        self.pushButton_1.setStyleSheet(  # "color: red;"
           'image : url(image/distance.png)')
        #m_img[0].load(":/newPrefix/image/distance.png");
        self.pushButton_2.setStyleSheet(  # "color: green;"
            'image:url(image/new.png)')

        self.pushButton_3.setStyleSheet(  # "color: blue;"
            'image:url(image/popular.png)')

        self.comboBox.addItem(' ')
        self.comboBox.addItem('서울')
        self.comboBox.addItem('부산')
        self.comboBox.addItem('대구')
        self.comboBox.addItem('인천')
        self.comboBox.addItem('광주')
        self.comboBox.addItem('대전')
        self.comboBox.addItem('울산')
        self.comboBox.addItem('경기')
        self.comboBox.addItem('강원')
        self.comboBox.addItem('충북')
        self.comboBox.addItem('충남')
        self.comboBox.addItem('경북')
        self.comboBox.addItem('경남')
        self.comboBox.addItem('전북')
        self.comboBox.addItem('전남')
        self.comboBox.addItem('제주')
        # cb.move(50, 50)

        self.comboBox.activated[str].connect(self.onActivated)

    def OptionClicked_1(self):
        global tmp_option_data
        print('Click!!!!1')
        tmp_option_data = 2
        print(tmp_option_data)
        if tmp_region_data == 0:
            self.label_1.setText('지역을 선택하세요!')
        else:
            self.label_1.setText('선택 완료')

    def OptionClicked_2(self):
        global tmp_option_data
        print('Click!!!!1')
        tmp_option_data = 1
        print(tmp_option_data)
        if tmp_region_data == 0:
            self.label_1.setText('지역을 선택하세요!')
        else:
            self.label_1.setText('선택 완료')

    def OptionClicked_3(self):
        global tmp_option_data
        print('Click!!!!1')
        tmp_option_data = 3
        print(tmp_option_data)
        if tmp_region_data == 0:
            self.label_1.setText('지역을 선택하세요!')
        else:
            self.label_1.setText('선택 완료')

    def onActivated(self, text):
        global tmp_region_data
        global tmp_option_data

        #self.label.adjustSize()

        if text == " ":
            tmp_region_data = 0
        elif text == "서울":
            tmp_region_data = 1
        elif text == "부산":
            tmp_region_data = 6
        elif text == "대구":
            tmp_region_data = 4
        elif text == "인천":
            tmp_region_data = 2
        elif text == "광주":
            tmp_region_data = 5
        elif text == "대전":
            tmp_region_data = 3
        elif text == "울산":
            tmp_region_data = 7
        elif text == "세종":
            tmp_region_data = 8
        elif text == "경기":
            tmp_region_data = 31
        elif text == "강원":
            tmp_region_data = 32
        elif text == "충북":
            tmp_region_data = 33
        elif text == "충남":
            tmp_region_data = 34
        elif text == "경북":
            tmp_region_data = 35
        elif text == "경남":
            tmp_region_data = 36
        elif text == "전북":
            tmp_region_data = 37
        elif text == "전남":
            tmp_region_data = 38
        elif text == "제주":
            tmp_region_data = 39

        if tmp_option_data == 0:
            self.label_1.setText('축제 정렬 기준을 선택하세요!')
        else :
            self.label_1.setText('선택 완료')


        print(tmp_region_data)


    def applyButton(self):

       if tmp_option_data == 0:
           self.label_1.setText('축제 정렬 기준을 선택하세요!')
       elif tmp_region_data == 0:
           self.label_1.setText('지역을 선택하세요!')
       else :

           #self.pushButton_4.clicked.connect(QCoreApplication.instance().quit)

           self.close()
           choice.open_navi(str(tmp_region_data), str(tmp_option_data))
          # QCoreApplication.instance().quit
       #    QMessageBox.about(self, "message", "정렬 기준 : " + str(tmp_option_data) + " " + "지역 : " + str(tmp_region_data))
       #    print('축제 정렬 기준 : ' + str(tmp_option_data))
       #    print('지역 선택 : ' + str(tmp_region_data))


app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
