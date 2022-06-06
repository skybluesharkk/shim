import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QPushButton,QLabel,QVBoxLayout,qApp,QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon,QPainter,QPen,QColor,QBrush
from PyQt5.QtCore import QCoreApplication,Qt,QDate
from student import student

class secondwindow(QWidget):

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

        btn = QPushButton('선택 완료', self)
        btn.move(80, 490)
        btn.resize(240, 60)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn1 = QPushButton('1', self)
        btn1.move(80, 40)
        btn1.resize(240,60)
        btn1.clicked.connect(self.btn_clicked)

        btn2 = QPushButton('2', self)
        btn2.move(80, 115)
        btn2.resize(240,60)
        btn2.clicked.connect(self.btn_clicked)

        btn3 = QPushButton('3', self)
        btn3.move(80, 185)
        btn3.resize(240,60)
        btn3.clicked.connect(self.btn_clicked)

        btn4 = QPushButton('4', self)
        btn4.move(80, 255)
        btn4.resize(240,60)
        btn4.clicked.connect(self.btn_clicked)

        btn5 = QPushButton('5', self)
        btn5.move(80, 325)
        btn5.resize(240,60)
        btn5.clicked.connect(self.btn_clicked)

        btn6 = QPushButton('6', self)
        btn6.move(80, 395)
        btn6.resize(240,60)
        btn6.clicked.connect(self.btn_clicked)


        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('시간권 선택')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(400,400,400,600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(Qt.darkGray)
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0,0,400,600)

        qp.setBrush(Qt.gray)
        qp.setPen(QPen(Qt.black,3))
        qp.drawRect(40,20,320,550)


    def btn_clicked(self):
        print('선택되었습니다')

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', '이름을 입력하세요')

        if ok:
            self.le.setText(str(text)+'님 환영합니다')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = secondwindow()
    sys.exit(app.exec_())