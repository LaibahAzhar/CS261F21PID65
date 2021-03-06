from PyQt5 import QtCore, QtGui, QtWidgets
from filter import filter_Form
from Seting import Set_Form
import sys, Search, subprocess

class search_Form(object):

    def filter(self):
         self.window2 = QtWidgets.QMainWindow()
         self.ui=filter_Form()
         self.ui.setupUi(self.window2)
         self.window2.show()

    def set(self):
         self.window2 = QtWidgets.QMainWindow()
         self.ui= Set_Form()
         self.ui.setupUi(self.window2)
         self.window2.show()

    def open(self):
        subprocess.Popen (r'explorer/select,"C:/Users/hp/OneDrive/Documents/CS261F21PID65/"')
    def setupUi(self, Form):
        Form.setObjectName("Search")
        Form.resize(625, 624)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 40, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 30, 511, 171))
        self.label.setStyleSheet("border-image:url(:/img/search);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 199, 511, 261))
        self.label_3.setStyleSheet("background-color:rgb(39, 39, 39);\n"
"border-bottom-right-radius: 15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(210, 210, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 260, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(0, 0, 2);\n"
"border:none;\n"
"border-bottom:2px solid qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.556818 rgba(4, 41, 36, 255), stop:0.852273 rgba(20, 50, 147, 255));\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(0, 420, 171, 40))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
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
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(130, 70, 230, 81))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,125);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(150, 80, 241, 61))
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
        self.pushButton_2.setGeometry(QtCore.QRect(170, 420, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border:0;\n"
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
"\n"
"QPushButton#pushButton_2{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,255), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 420, 181, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
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
"\n"
"QPushButton#pushButton_2{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_3{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border-bottom-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.set)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 330, 181, 40))
        self.pushButton_4.clicked.connect(self.filter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
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
"\n"
"QPushButton#pushButton_2{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border:0;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_3{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,255);\n"
"    border-bottom-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#pushButton_4{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.989, y2:0, stop:0.420455 rgba(4, 38, 41, 255), stop:0.715909 rgba(65, 12, 84, 255));\n"
"    color:rgba(255,255,255,255);\n"
"    border-top-left-radius:30px;\n"
"    border-bottom-right-radius:30px;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Search"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Search Text"))
        self.pushButton.setText(_translate("Form", "History"))
        self.label_7.setText(_translate("Form", "Twitter Squeaker"))
        self.pushButton_2.setText(_translate("Form", "Saved Files"))
        self.pushButton_3.setText(_translate("Form", "Settings"))
        self.pushButton_4.setText(_translate("Form", "Squeak Now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = search_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

