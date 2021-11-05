from PyQt5 import QtCore, QtGui, QtWidgets
import sys,regres
import csv

class Reg_Form(object):
    
    
    def setupUi(self, Form):
        Form.setObjectName("Create Account")
        Form.resize(625, 564)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 60, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/img/register);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("border-image:url(:/image/reg);\n"
"background-color:rgba(0,0,0,80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(289, 30, 221, 430))
        self.label_3.setStyleSheet("background-color:rgb(39, 39, 39);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 30, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0,200);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 280, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0,200);;\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(190, 390, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border-radius:15px;\n"
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
        self.pushButton.clicked.connect(self.save_info)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 250, 81))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,125);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(70, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Baby Child")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 220, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0, 0, 25);\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 270, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0, 0, 25);\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 320, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0, 0, 25);\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 170, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0, 0, 25);\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_5.setStyleSheet("background-color:rgba(255,255,255,15);\n"
"border-top-left-radius: 50px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Register", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Twitter </p><p align=\"center\">Credentials</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Sign Up"))
        self.label_7.setText(_translate("Form", "Twitter Squeaker"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "E-mail"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "User Name"))
        
    def save_info(self):
        self.username=self.lineEdit_6.text()
        self.email=self.lineEdit_3.text()
        if self.lineEdit_4.text()==self.lineEdit_5.text():
            self.password = self.lineEdit_4.text()    
        else:
                msg = QtCore.QMessageLogContext()
                msg.setIcon(QtCore.QMessageLogContext.Critical)
                msg.setText("Passwords does not Match")
                msg.setWindowTitle("Warning !")
                msg.setStandardButtons(QtCore.QMessageLogContext.Ok | QtCore.QMessageLogContext.Cancel)
                
        self.Tuser= self.lineEdit.text()
        self.Tpass=self.lineEdit_2.text()
                
        with open('users.csv', 'w', encoding='UTF8', newline='') as f:
                header = ['UserName','E-mail','Password','Twitter User','Twitter Password']
                data =[self.username,self.email,self.password,self.Tuser,self.Tpass]
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
        
        print('Close button pressed')
        import sys
        sys.exit(0)
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Reg_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
