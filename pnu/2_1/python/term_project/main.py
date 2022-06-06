import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton,QLabel,QVBoxLayout,qApp,QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import QCoreApplication, Qt, QDate
from student import student
from time2 import *

class RGB(QColor):
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue)

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('회원정보 등록', self)
        self.btn.move(300, 350)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(300, 400)
        self.le.resize(200,50)

        btn = QPushButton('사물함',self)
        btn.move(40,600)
        btn.resize(160,120)
        btn.clicked.connect(self.showDialog)

        btn = QPushButton('신발장', self)
        btn.move(220, 600)
        btn.resize(160, 120)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn = QPushButton('종료하기', self)
        btn.move(400, 600)
        btn.resize(160, 120)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn1 = QPushButton('1', self)
        btn1.move(60, 40)
        btn1.resize(80,80)
        btn1.clicked.connect(self.btn_clicked)

        btn2 = QPushButton('2', self)
        btn2.move(60, 120)
        btn2.resize(80,80)
        btn2.clicked.connect(self.btn_clicked)

        btn3 = QPushButton('3', self)
        btn3.move(60, 200)
        btn3.resize(80,80)
        btn3.clicked.connect(self.btn_clicked)

        btn4 = QPushButton('4', self)
        btn4.move(60, 280)
        btn4.resize(80,80)
        btn4.clicked.connect(self.btn_clicked)

        btn5 = QPushButton('5', self)
        btn5.move(60, 360)
        btn5.resize(80,80)
        btn5.clicked.connect(self.btn_clicked)

        btn6 = QPushButton('6', self)
        btn6.move(60, 440)
        btn6.resize(80,80)
        btn6.clicked.connect(self.btn_clicked)

        btn7 = QPushButton('7', self)
        btn7.move(170, 40)
        btn7.resize(80, 80)
        btn7.clicked.connect(self.btn_clicked)

        btn8 = QPushButton('8', self)
        btn8.move(170, 120)
        btn8.resize(80, 80)
        btn8.clicked.connect(self.btn_clicked)

        btn9 = QPushButton('9', self)
        btn9.move(170, 200)
        btn9.resize(80, 80)
        btn9.clicked.connect(self.btn_clicked)

        btn10 = QPushButton('10', self)
        btn10.move(170, 280)
        btn10.resize(80, 80)
        btn10.clicked.connect(self.btn_clicked)

        btn11 = QPushButton('11', self)
        btn11.move(170, 360)
        btn11.resize(80, 80)
        btn11.clicked.connect(self.btn_clicked)

        btn12 = QPushButton('12', self)
        btn12.move(170, 440)
        btn12.resize(80, 80)
        btn12.clicked.connect(self.btn_clicked)

        btnz1 = QPushButton('작심1', self)
        btnz1.move(320, 40)
        btnz1.resize(80, 80)
        btnz1.clicked.connect(self.btn_clicked)

        btnz2 = QPushButton('작심2', self)
        btnz2.move(320, 120)
        btnz2.resize(80, 80)
        btnz2.clicked.connect(self.btn_clicked)

        btnz3 = QPushButton('작심3', self)
        btnz3.move(320, 200)
        btnz3.resize(80, 80)
        btnz3.clicked.connect(self.btn_clicked)

        btnz4 = QPushButton('작심4', self)
        btnz4.move(470, 40)
        btnz4.resize(80, 80)
        btnz4.clicked.connect(self.btn_clicked)

        btnz5 = QPushButton('작심5', self)
        btnz5.move(470, 120)
        btnz5.resize(80, 80)
        btnz5.clicked.connect(self.btn_clicked)

        btnz6 = QPushButton('작심6', self)
        btnz6.move(470, 200)
        btnz6.resize(80, 80)
        btnz6.clicked.connect(self.btn_clicked2)


        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('작심 스터디카페')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(600,600,600,800)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(153,51,000))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0,0,600,800)

        qp.setBrush(Qt.gray)
        qp.setPen(QPen(Qt.black,3))
        qp.drawRect(40,20,230,520)

        qp.setBrush(Qt.gray)
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(300,20, 270, 300)

    def btn_clicked(self):
        print('선택되었습니다')

    def btn_clicked2(self):
        test.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', '이름을 입력하세요')

        if ok:
            self.le.setText(str(text)+'님 환영합니다')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())