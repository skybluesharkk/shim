import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from RGB import RGB

class lockerroom(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('1번', self)
        btn1.move(80, 40)
        btn1.resize(80, 80)
        btn1.clicked.connect(self.btn_clicked1)

        btn2 = QPushButton('2번', self)
        btn2.move(80, 140)
        btn2.resize(80, 80)
        btn2.clicked.connect(self.btn_clicked3)

        btn3 = QPushButton('3번', self)
        btn3.move(80, 240)
        btn3.resize(80, 80)
        btn3.clicked.connect(self.btn_clicked3)

        btn4 = QPushButton('4번', self)
        btn4.move(180, 40)
        btn4.resize(80, 80)
        btn4.clicked.connect(self.btn_clicked4)

        btn5 = QPushButton('5번', self)
        btn5.move(180, 140)
        btn5.resize(80, 80)
        btn5.clicked.connect(self.btn_clicked5)

        btn6 = QPushButton('6번', self)
        btn6.move(180, 240)
        btn6.resize(80, 80)
        btn6.clicked.connect(self.btn_clicked6)

        self.setWindowTitle('사물함 선택')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(400, 400, 340, 400)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 340, 400)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(40, 20, 260, 320)

    def btn_clicked1(self):
        my_study["사물함"].append("1번")
        self.close()

    def btn_clicked2(self):
        my_study["사물함"].append("2번")
        self.close()

    def btn_clicked3(self):
        my_study["사물함"].append("3번")
        self.close()

    def btn_clicked4(self):
        my_study["사물함"].append("4번")
        self.close()

    def btn_clicked5(self):
        my_study["사물함"].append("5번")
        self.close()

    def btn_clicked6(self):
        my_study["사물함"].append("6번")
        self.close()

    def btn_clicked7(self):
        self.close()


class shoes(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        btn = QPushButton('뒤로 가기', self)
        btn.move(80, 490)
        btn.resize(240, 60)
        btn.clicked.connect(self.btn_clicked7)

        btn1 = QPushButton('1번', self)
        btn1.move(80, 40)
        btn1.resize(80, 80)
        btn1.clicked.connect(self.btn_clicked1)

        btn2 = QPushButton('2번', self)
        btn2.move(80, 140)
        btn2.resize(80, 80)
        btn2.clicked.connect(self.btn_clicked2)

        btn3 = QPushButton('3번', self)
        btn3.move(80, 240)
        btn3.resize(80, 80)
        btn3.clicked.connect(self.btn_clicked3)

        btn4 = QPushButton('4번', self)
        btn4.move(180, 40)
        btn4.resize(80, 80)
        btn4.clicked.connect(self.btn_clicked4)

        btn5 = QPushButton('5번', self)
        btn5.move(180, 140)
        btn5.resize(80, 80)
        btn5.clicked.connect(self.btn_clicked5)

        btn6 = QPushButton('6번', self)
        btn6.move(180, 240)
        btn6.resize(80, 80)
        btn6.clicked.connect(self.btn_clicked6)

        self.setWindowTitle('신발장 선택')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(400, 400, 340, 400)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 340, 400)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(40, 20, 260, 320)

    def btn_clicked1(self):
        my_study["신발장"].append("1번")
        self.close()

    def btn_clicked2(self):
        my_study["신발장"].append("2번")
        self.close()

    def btn_clicked3(self):
        my_study["신발장"].append("3번")
        self.close()

    def btn_clicked4(self):
        my_study["신발장"].append("4번")
        self.close()

    def btn_clicked5(self):
        my_study["신발장"].append("5번")
        self.close()

    def btn_clicked6(self):
        my_study["신발장"].append("6번")
        self.close()

    def btn_clicked7(self):
        self.close()

class ppay(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.le = QLineEdit(self)
        self.le.move(100, 60)
        self.le.resize(150, 70)
        self.le.setText('결제가 완료되었습니다!')

        self.setWindowTitle('최종 결제')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(400, 400, 340, 200)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 340, 200)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(40, 20, 260, 160)

class secondwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        btn = QPushButton('뒤로 가기', self)
        btn.move(80, 490)
        btn.resize(240, 60)
        btn.clicked.connect(self.btn_clicked7)

        btn1 = QPushButton('1시간\n(1000원)', self)
        btn1.move(80, 40)
        btn1.resize(240, 60)
        btn1.clicked.connect(self.btn_clicked1)

        btn2 = QPushButton('2시간\n(2000원)', self)
        btn2.move(80, 115)
        btn2.resize(240, 60)
        btn2.clicked.connect(self.btn_clicked2)

        btn3 = QPushButton('3시간\n(3000원)', self)
        btn3.move(80, 185)
        btn3.resize(240, 60)
        btn3.clicked.connect(self.btn_clicked3)

        btn4 = QPushButton('4시간\n(4000원)', self)
        btn4.move(80, 255)
        btn4.resize(240, 60)
        btn4.clicked.connect(self.btn_clicked4)

        btn5 = QPushButton('5시간\n(5000원)', self)
        btn5.move(80, 325)
        btn5.resize(240, 60)
        btn5.clicked.connect(self.btn_clicked5)

        btn6 = QPushButton('6시간\n(6000원)', self)
        btn6.move(80, 395)
        btn6.resize(240, 60)
        btn6.clicked.connect(self.btn_clicked6)

        self.setWindowTitle('시간권 선택')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(400, 400, 400, 600)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 400, 600)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(40, 20, 320, 550)

    def btn_clicked1(self):
        my_study["시간"].append("1시간")
        my_study["요금"].append("1000")
        self.close()

    def btn_clicked2(self):
        my_study["시간"].append("2시간")
        my_study["요금"].append("2000")

        self.close()

    def btn_clicked3(self):
        my_study["시간"].append("3시간")
        my_study["요금"].append("3000")
        self.close()

    def btn_clicked4(self):
        my_study["시간"].append("4시간")
        my_study["요금"].append("4000")
        self.close()

    def btn_clicked5(self):
        my_study["시간"].append("5시간")
        my_study["요금"].append("5000")
        self.close()

    def btn_clicked6(self):
        my_study["시간"].append("6시간")
        my_study["요금"].append("6000")
        self.close()

    def btn_clicked7(self):
        self.close()

class firstwindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.sub_window = secondwindow()
        self.sub_window2 = lockerroom()
        self.sub_window3 = shoes()
        self.sub_window4 = ppay()

        btn = QPushButton('사물함', self)
        btn.move(40, 550)
        btn.resize(160, 120)
        btn.clicked.connect(self.sub_window2.show)

        btn = QPushButton('신발장', self)
        btn.move(220, 550)
        btn.resize(160, 120)
        btn.clicked.connect(self.sub_window3.show)

        btn = QPushButton('종료하기', self)
        btn.move(400, 550)
        btn.resize(160, 120)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn = QPushButton('결제하기', self)
        btn.move(400, 400)
        btn.resize(160, 120)
        btn.clicked.connect(self.sub_window4.show)

        btn = QPushButton('영수증 출력하기', self)
        btn.move(400, 340)
        btn.resize(160, 40)
        btn.clicked.connect(self.btn_clicked99)

        self.le = QLineEdit(self)
        self.le.move(40, 680)
        self.le.resize(520, 50)
        self.le.setText(str(my_study)) #회원의 현재 결정 상태를 쉽게 볼 수 있도록 아래에 표현하는 코드입니다

        btn1 = QPushButton('1', self)
        btn1.move(60, 40)
        btn1.resize(80, 80)
        btn1.clicked.connect(self.btn_clicked)
        btn1.clicked.connect(self.sub_window.show)

        btn2 = QPushButton('2', self)
        btn2.move(60, 120)
        btn2.resize(80, 80)
        btn2.clicked.connect(self.btn_clicked2)
        btn2.clicked.connect(self.sub_window.show)

        btn3 = QPushButton('3', self)
        btn3.move(60, 200)
        btn3.resize(80, 80)
        btn3.clicked.connect(self.btn_clicked3)
        btn3.clicked.connect(self.sub_window.show)

        btn4 = QPushButton('4', self)
        btn4.move(60, 280)
        btn4.resize(80, 80)
        btn4.clicked.connect(self.btn_clicked4)
        btn4.clicked.connect(self.sub_window.show)

        btn5 = QPushButton('5', self)
        btn5.move(60, 360)
        btn5.resize(80, 80)
        btn5.clicked.connect(self.btn_clicked5)
        btn5.clicked.connect(self.sub_window.show)

        btn6 = QPushButton('6', self)
        btn6.move(60, 440)
        btn6.resize(80, 80)
        btn6.clicked.connect(self.btn_clicked6)
        btn6.clicked.connect(self.sub_window.show)

        btn7 = QPushButton('7', self)
        btn7.move(170, 40)
        btn7.resize(80, 80)
        btn7.clicked.connect(self.btn_clicked7)
        btn7.clicked.connect(self.sub_window.show)

        btn8 = QPushButton('8', self)
        btn8.move(170, 120)
        btn8.resize(80, 80)
        btn8.clicked.connect(self.btn_clicked8)
        btn8.clicked.connect(self.sub_window.show)

        btn9 = QPushButton('9', self)
        btn9.move(170, 200)
        btn9.resize(80, 80)
        btn9.clicked.connect(self.btn_clicked9)
        btn9.clicked.connect(self.sub_window.show)

        btn10 = QPushButton('10', self)
        btn10.move(170, 280)
        btn10.resize(80, 80)
        btn10.clicked.connect(self.btn_clicked10)
        btn10.clicked.connect(self.sub_window.show)

        btn11 = QPushButton('11', self)
        btn11.move(170, 360)
        btn11.resize(80, 80)
        btn11.clicked.connect(self.btn_clicked11)
        btn11.clicked.connect(self.sub_window.show)

        btn12 = QPushButton('12', self)
        btn12.move(170, 440)
        btn12.resize(80, 80)
        btn12.clicked.connect(self.btn_clicked12)
        btn12.clicked.connect(self.sub_window.show)

        btnz1 = QPushButton('심심1', self)
        btnz1.move(320, 40)
        btnz1.resize(80, 80)
        btnz1.clicked.connect(self.btn_clicked13)
        btnz1.clicked.connect(self.sub_window.show)

        btnz2 = QPushButton('심심2', self)
        btnz2.move(320, 120)
        btnz2.resize(80, 80)
        btnz2.clicked.connect(self.btn_clicked14)
        btnz2.clicked.connect(self.sub_window.show)

        btnz3 = QPushButton('심심3', self)
        btnz3.move(320, 200)
        btnz3.resize(80, 80)
        btnz3.clicked.connect(self.btn_clicked15)
        btnz3.clicked.connect(self.sub_window.show)

        btnz4 = QPushButton('심심4', self)
        btnz4.move(470, 40)
        btnz4.resize(80, 80)
        btnz4.clicked.connect(self.btn_clicked16)
        btnz4.clicked.connect(self.sub_window.show)

        btnz5 = QPushButton('심심5', self)
        btnz5.move(470, 120)
        btnz5.resize(80, 80)
        btnz5.clicked.connect(self.btn_clicked17)
        btnz5.clicked.connect(self.sub_window.show)

        btnz6 = QPushButton('심심6', self)
        btnz6.move(470, 200)
        btnz6.resize(80, 80)
        btnz6.clicked.connect(self.btn_clicked18)
        btnz6.clicked.connect(self.sub_window.show)

        btn = QPushButton('결정', self)
        btn.move(300, 450)
        btn.resize(40, 40)
        btn.clicked.connect(self.btn_clicked00)


        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('심심 스터디')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(800, 200, 600, 800)

    def btn_clicked99(self):
        price = list(map(int, my_study["요금"]))
        result = sum(price)
        f = open("영수증.txt",'w')
        data = "최종 요금은 %d원입니다.\n " %result
        f.write(data)
        f.close()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 600, 800)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(40, 20, 230, 520)

        qp.setBrush(RGB(247, 174, 99))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(300, 20, 270, 300)

    def btn_clicked(self):
        my_study["좌석"].append("1")
        self.le.setText(str(my_study))

    def btn_clicked2(self):
        my_study["좌석"].append("2")
        self.le.setText(str(my_study))

    def btn_clicked3(self):
        my_study["좌석"].append("3")
        self.le.setText(str(my_study))

    def btn_clicked4(self):
        my_study["좌석"].append("4")
        self.le.setText(str(my_study))

    def btn_clicked5(self):
        my_study["좌석"].append("5")
        self.le.setText(str(my_study))

    def btn_clicked6(self):
        my_study["좌석"].append("6")
        self.le.setText(str(my_study))

    def btn_clicked7(self):
        my_study["좌석"].append("7")
        self.le.setText(str(my_study))

    def btn_clicked8(self):
        my_study["좌석"].append("8")
        self.le.setText(str(my_study))

    def btn_clicked9(self):
        my_study["좌석"].append("9")
        self.le.setText(str(my_study))

    def btn_clicked10(self):
        my_study["좌석"].append("10")
        self.le.setText(str(my_study))

    def btn_clicked11(self):
        my_study["좌석"].append("11")
        self.le.setText(str(my_study))

    def btn_clicked12(self):
        my_study["좌석"].append("12")
        self.le.setText(str(my_study))

    def btn_clicked13(self):
        my_study["좌석"].append("작심1")
        self.le.setText(str(my_study))

    def btn_clicked14(self):
        my_study["좌석"].append("작심2")
        self.le.setText(str(my_study))

    def btn_clicked15(self):
        my_study["좌석"].append("작심3")
        self.le.setText(str(my_study))

    def btn_clicked16(self):
        my_study["좌석"].append("작심4")
        self.le.setText(str(my_study))

    def btn_clicked17(self):
        my_study["좌석"].append("작심5")
        self.le.setText(str(my_study))

    def btn_clicked18(self):
        my_study["좌석"].append("작심6")
        self.le.setText(str(my_study))

    def btn_clicked00(self):
        my_study["요금"].append("0")
        self.le.setText(str(my_study))
        price=list(map(int,my_study["요금"]))
        result = sum(price)
        print(result)
#최종금액을 표현하였으나 gui상으로 표시되지 않고 콘솔 상에만 출력합니다,,,

    def show_new_window(self, checked):
        self.secondwindow.show()
        self.hide()

    def btn_clicked34(self, checked):
        self.ppay.show()

class login(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.sub_window = firstwindow()
        self.btn = QPushButton('회원정보 등록', self)
        self.btn.move(50, 50)
        self.btn.resize(200, 50)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(50, 125)
        self.le.resize(200, 50)

        btn10 = QPushButton('좌석선택으로 넘어가기', self)
        btn10.move(50, 200)
        btn10.resize(200, 50)
        btn10.clicked.connect(self.sub_window.show)

        self.setWindowTitle('심심 스터디')
        self.setWindowIcon(QIcon('작심.jpg'))
        self.setGeometry(800, 200, 300, 300)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(RGB(20, 189, 227))
        qp.setPen(QPen(Qt.black, 3))
        qp.drawRect(0, 0, 600, 700)

    def show_new_window(self, checked):
        self.firstwindow().show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, '심심 스터디', '이름을 입력하세요')

        if ok:
            self.le.setText(str(text) + '님 환영합니다')
            my_study["이름"].append(str(text))

if __name__ == '__main__':
    my_study = {"이름":[], "좌석":[], "시간":[] , "사물함":[], "신발장":[], "요금":[] }
    app = QApplication([])
    window = login()
    window.show()
    sys.exit(app.exec_())
