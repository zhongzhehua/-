import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from kxjsq_ui import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    op_str = []
    show_op = ""
    input_num = ""

    xy = False
    xy_ds = ""
    xy_mc = ""
    sanjiao = True

    def point_(self):
        if '.' not in self.input_num:
            self.input_num = self.input_num + '.'
            self.showNum()

    def num_1(self):
        self.input_num = self.input_num + '1'
        self.showNum()

    def num_2(self):
        self.input_num = self.input_num + '2'
        self.showNum()

    def num_3(self):
        self.input_num = self.input_num + '3'
        self.showNum()

    def num_4(self):
        self.input_num = self.input_num + '4'
        self.showNum()

    def num_5(self):
        self.input_num = self.input_num + '5'
        self.showNum()

    def num_6(self):
        self.input_num = self.input_num + '6'
        self.showNum()

    def num_7(self):
        self.input_num = self.input_num + '7'
        self.showNum()

    def num_8(self):
        self.input_num = self.input_num + '8'
        self.showNum()

    def num_9(self):
        self.input_num = self.input_num + '9'
        self.showNum()

    def num_0(self):
        self.input_num = self.input_num + '0'
        self.showNum()

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showLogo()
        self.pushButton_1.clicked.connect(lambda: self.num_1())
        self.pushButton_2.clicked.connect(lambda: self.num_2())
        self.pushButton_3.clicked.connect(lambda: self.num_3())
        self.pushButton_4.clicked.connect(lambda: self.num_4())
        self.pushButton_5.clicked.connect(lambda: self.num_5())
        self.pushButton_6.clicked.connect(lambda: self.num_6())
        self.pushButton_7.clicked.connect(lambda: self.num_7())
        self.pushButton_8.clicked.connect(lambda: self.num_8())
        self.pushButton_9.clicked.connect(lambda: self.num_9())
        self.pushButton_0.clicked.connect(lambda: self.num_0())
        self.pushButton_dian.clicked.connect(lambda: self.point_())
        self.pushButton_sin.clicked.connect(lambda: self.op_sin())
        self.pushButton_cos.clicked.connect(lambda: self.op_cos())
        self.pushButton_tan.clicked.connect(lambda: self.op_tan())
        self.pushButton_arcsin.clicked.connect(lambda: self.op_arcsin())
        self.pushButton_arccos.clicked.connect(lambda: self.op_arccos())
        self.pushButton_arctan.clicked.connect(lambda: self.op_arctan())
        self.pushButton_jia.clicked.connect(lambda: self.op_jia())
        self.pushButton_jian.clicked.connect(lambda: self.op_jian())
        self.pushButton_cheng.clicked.connect(lambda: self.op_cheng())
        self.pushButton_chu.clicked.connect(lambda: self.op_chu())
        self.pushButton_jiecheng.clicked.connect(lambda: self.op_jiecheng())
        self.pushButton_c.clicked.connect(lambda: self.op_c())
        self.pushButton_ce.clicked.connect(lambda: self.op_ce())
        self.pushButton_tw.clicked.connect(lambda: self.op_tw())
        self.pushButton_pai.clicked.connect(lambda: self.op_pi())
        self.pushButton_e.clicked.connect(lambda: self.op_e())
        self.pushButton_kf.clicked.connect(lambda: self.op_kf())
        self.pushButton_x_2.clicked.connect(lambda: self.op_x_2())
        self.pushButton_x_y.clicked.connect(lambda: self.op_x_y())
        self.pushButton_log.clicked.connect(lambda: self.op_log())
        self.pushButton_dengyu.clicked.connect(lambda: self.op_dengyu())
        self.pushButton_tab.clicked.connect(lambda: self.op_tab())
        self.pushButton_arcsin.hide()
        self.pushButton_arccos.hide()
        self.pushButton_arctan.hide()

    def showNum(self):
        self.label_now.setText(self.input_num)

    def showLogo(self):
        logo_jpg = QPixmap("logo.jpg")
        self.label_logo.setPixmap(logo_jpg)

    def showHis(self):
        op_line = ""
        for i in self.op_str:
            op_line = op_line + i
        self.label_his.setText(self.show_op)
        return op_line

    def op_jia(self):
        if self.show_op == "":
            self.show_op = self.show_op + self.input_num
        elif self.show_op[-1] != ")":
            self.show_op = self.show_op + self.input_num
        self.op_x_y_mc()
        self.op_str.append(self.input_num)
        self.input_num = ""
        self.op_str.append("+")
        self.show_op = self.show_op + "+"
        self.label_now.setText("+")
        self.showHis()

    def op_jian(self):

        if self.show_op == "":
            self.show_op = self.show_op + self.input_num
        elif self.show_op[-1] != ")":
            self.show_op = self.show_op + self.input_num
        self.op_x_y_mc()
        self.op_str.append(self.input_num)
        self.input_num = ""
        self.op_str.append("-")
        self.show_op = self.show_op + "-"
        self.label_now.setText("-")
        self.showHis()

    def op_cheng(self):

        if self.show_op == "":
            self.show_op = self.show_op + self.input_num
        elif self.show_op[-1] != ")":
            self.show_op = self.show_op + self.input_num
        self.op_x_y_mc()
        self.op_str.append(self.input_num)
        self.input_num = ""
        self.op_str.append("*")
        self.show_op = self.show_op + "×"
        self.label_now.setText("×")
        self.showHis()

    def op_chu(self):

        if self.show_op == "":
            self.show_op = self.show_op + self.input_num
        elif self.show_op[-1] != ")":
            self.show_op = self.show_op + self.input_num
        self.op_x_y_mc()
        self.op_str.append(self.input_num)
        self.input_num = ""
        self.op_str.append("/")
        self.show_op = self.show_op + "÷"
        self.label_now.setText("÷")
        self.showHis()

    def op_dengyu(self):
        if self.show_op[-1] != ")":
            self.show_op = self.show_op + self.input_num
        self.op_x_y_mc()
        self.op_str.append(self.input_num)
        self.show_op = self.show_op + "="

        his_str = self.showHis()
        self.label_now.setText(str(eval(his_str)))

        self.op_str = []
        self.show_op = ""
        self.input_num = str(eval(his_str))

    def op_sin(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "sin(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "sin(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "sin(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.sin(eval(self.input_num)*math.pi/180), 6))
            self.showHis()
            self.showNum()

    def op_cos(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "cos(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "cos(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "cos(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.cos(eval(self.input_num)*math.pi/180), 6))
            self.showHis()
            self.showNum()

    def op_tan(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "tan(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "tan(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "tan(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.tan(eval(self.input_num)*math.pi/180), 6))
            self.showHis()
            self.showNum()

    def op_arcsin(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "arcsin(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "arcsin(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "arcsin(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.degrees(math.asin(eval(self.input_num))), 2))
            self.showHis()
            self.showNum()

    def op_arccos(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "arccos(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "arccos(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "arccos(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.degrees(math.acos(eval(self.input_num))), 2))
            self.showHis()
            self.showNum()

    def op_arctan(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "arctan(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "arctan(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "arctan(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.degrees(math.atan(eval(self.input_num))), 2))
            self.showHis()
            self.showNum()

    def op_jiecheng(self):
        if isinstance(eval(self.input_num), int):
            if self.input_num != "":
                if self.show_op == "":
                    self.show_op = self.show_op + "(" + self.input_num + "!)"
                elif self.show_op[-1] != ")":
                    self.show_op = self.show_op + "(" + self.input_num + "!)"
                elif self.show_op[-1] == ")":
                    npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                               self.show_op.rfind("÷"))
                    self.show_op = self.show_op[:npox + 1] + "(" + self.show_op[npox + 1:] + "!)"
                self.input_num = str(self.jiecheng(eval(self.input_num)))
                self.showHis()
                self.showNum()
        else:
            self.label_now.setText("类型错误")

    def op_c(self):
        self.op_str = []
        self.show_op = ""
        self.label_his.setText("")
        self.input_num = ""
        self.showNum()

    def op_ce(self):
        self.input_num = ""
        self.showNum()

    def op_tw(self):
        self.input_num = self.input_num[:-1]
        self.showNum()

    def op_pi(self):
        self.input_num = str(math.pi)
        self.showNum()

    def op_e(self):
        self.input_num = str(math.e)
        self.showNum()

    def op_kf(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "√(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "√(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "√(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.sqrt(eval(self.input_num)), 6))
            self.showHis()
            self.showNum()

    def op_x_2(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "sqr(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "sqr(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "sqr(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.pow(eval(self.input_num), 2), 6))
            self.showHis()
            self.showNum()

    def op_x_y(self):
        if self.xy == False:
            self.xy_ds = self.input_num
            if self.show_op == "":
                self.show_op = self.show_op + self.xy_ds + "^"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + self.xy_ds + "^"
            else:
                self.show_op = self.show_op + "^"
            self.showHis()
            self.input_num = ""
            self.label_now.setText("^")
            self.xy = True

    def op_x_y_mc(self):
        if self.xy:
            self.xy_mc = self.input_num
            self.showHis()
            self.input_num = str(math.pow(eval(self.xy_ds), eval(self.xy_mc)))
            self.showNum()
            self.xy = False

    def op_log(self):
        if self.input_num != "":
            if self.show_op == "":
                self.show_op = self.show_op + "log(" + self.input_num + ")"
            elif self.show_op[-1] != ")":
                self.show_op = self.show_op + "log(" + self.input_num + ")"
            elif self.show_op[-1] == ")":
                npox = max(self.show_op.rfind("+"), self.show_op.rfind("-"), self.show_op.rfind("×"),
                           self.show_op.rfind("÷"))
                self.show_op = self.show_op[:npox + 1] + "log(" + self.show_op[npox + 1:] + ")"
            self.input_num = str(round(math.log(eval(self.input_num),10), 6))
            self.showHis()
            self.showNum()

    def op_tab(self):
        if self.sanjiao:
            self.pushButton_sin.hide()
            self.pushButton_cos.hide()
            self.pushButton_tan.hide()
            self.pushButton_arcsin.show()
            self.pushButton_arccos.show()
            self.pushButton_arctan.show()
            self.sanjiao = False
            self.pushButton_tab.setText("↓")
        else:
            self.pushButton_sin.show()
            self.pushButton_cos.show()
            self.pushButton_tan.show()
            self.pushButton_arcsin.hide()
            self.pushButton_arccos.hide()
            self.pushButton_arctan.hide()
            self.sanjiao = True
            self.pushButton_tab.setText("↑")

    def jiecheng(self, numb):
        if numb == 1:
            return 1
        else:
            return numb * self.jiecheng(numb - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
