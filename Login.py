import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from register import Reg_Form
from searching import search_Form
import sys,resource

from searching import search_Form

class Ui_Form(object):

    def register(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui= Reg_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()
        
    def setupUi(self, Form):
        Form.setObjectName("Login")
        Form.setEnabled(True)
        Form.resize(625, 565)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/loginimg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgb(39, 39, 39);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(295, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(40, 40, 40);;\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(295, 215, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgb(40, 40, 40);;\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check_input)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(300, 270, 141, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 70, 230, 81))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,125);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(60, 80, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Baby Child")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(415, 40, 95, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    background-color:qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgb(255, 255, 255);\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_:pressed{\n"
"\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.register)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "Forgot Password?"))
        self.label_7.setText(_translate("Form", "Twitter Squeaker"))
        self.pushButton_2.setText(_translate("Form", "Create Account"))

    def check_input(self):
        with open('users.csv')as r:
                reader= csv.reader(r)
                for row in reader:
                        if(self.lineEdit.text()==row[0]):
                                if(self.lineEdit_2.text()==row[2]):
                                        
                                        self.window3 = QtWidgets.QMainWindow()
                                        self.ui=search_Form()
                                        self.ui.setupUi(self.window3)
                                        self.window3.show()
                                else:
                                        print("in Password")         
                        else:
                                print('in user')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
