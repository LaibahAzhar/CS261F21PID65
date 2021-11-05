from PyQt5 import QtCore, QtGui, QtWidgets
from Seting import Set_Form
import sys, filterres

class filter_Form(object):
        
    def set(self):
         self.window2 = QtWidgets.QMainWindow()
         self.ui= Set_Form()
         self.ui.setupUi(self.window2)
         self.window2.show()
    def setupUi(self, Form):
        Form.setObjectName("Filter Search")
        Form.resize(634, 565)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 30, 550, 500))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(0, 460, 171, 40))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 460, 181, 40))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 460, 181, 40))
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
"    border-bottom-right-radius:30px;\n"
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
        self.pushButton_4.setGeometry(QtCore.QRect(180, 410, 181, 40))
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
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.label_3.setStyleSheet("background-color:rgba(39, 39, 39,100);\n"
"border-bottom-right-radius: 40px;\n"
"border-top-left-radius: 40px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.label_5.setStyleSheet("background-color:rgba(39, 39, 39,100);\n"
"border-bottom-right-radius: 40px;\n"
"border-top-left-radius: 40px;\n"
"border-image:url(:/img/filter)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 160, 511, 241))
        self.widget_2.setStyleSheet("background-color: rgba(0,0,0,200);\n"
"border-radius:30px;")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 190, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.label_7.setObjectName("label_7")
        self.radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton.setGeometry(QtCore.QRect(140, 90, 82, 17))
        self.radioButton.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 140, 82, 17))
        self.radioButton_2.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 90, 82, 17))
        self.radioButton_3.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 140, 82, 17))
        self.radioButton_4.setStyleSheet("background-color:rgba(0, 0, 0,0);\n"
"color:rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(370, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(0, 0, 2);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgb(0, 0, 2);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 40, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgb(0, 0, 2);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(140, 190, 51, 22))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color:rgba(0, 0, 0,100);\n"
"border-radius:10px;\n"
"color:rgb(255,255,255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(210, 190, 121, 22))
        self.dateTimeEdit.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"color:rgb(255, 255, 255)")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 80, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgb(0, 0, 2);\n"
"border:none;\n"
"border-bottom:2px solid qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.556818 rgba(4, 41, 36, 255), stop:0.852273 rgba(20, 50, 147, 255));\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.widget_2.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Search"))
        self.pushButton.setText(_translate("Form", "History"))
        self.pushButton_2.setText(_translate("Form", "Saved Files"))
        self.pushButton_3.setText(_translate("Form", "Settings"))
        self.pushButton_4.setText(_translate("Form", "Squeak Now"))
        self.label.setText(_translate("Form", "Time"))
        self.label_2.setText(_translate("Form", "Category"))
        self.label_6.setText(_translate("Form", "Likes"))
        self.label_7.setText(_translate("Form", "Retweets"))
        self.radioButton.setText(_translate("Form", "Max to Min"))
        self.radioButton_2.setText(_translate("Form", "Max to Min"))
        self.radioButton_3.setText(_translate("Form", "Min to Max"))
        self.radioButton_4.setText(_translate("Form", "Min to Max"))
        self.lineEdit.setText(_translate("Form", "Minimum"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Search Text"))
        self.lineEdit_3.setText(_translate("Form", "Minimum"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Search Text"))
        self.lineEdit_4.setText(_translate("Form", "Search By Category Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Search Text"))
        self.comboBox.setPlaceholderText(_translate("Form", "Time"))
        self.comboBox.setItemText(0, _translate("Form", "1hr Ago"))
        self.comboBox.setItemText(1, _translate("Form", "2hrs Ago"))
        self.comboBox.setItemText(2, _translate("Form", "4hrs Ago"))
        self.comboBox.setItemText(3, _translate("Form", "6hrs Ago"))
        self.comboBox.setItemText(4, _translate("Form", "10hrs Ago"))
        self.comboBox.setItemText(5, _translate("Form", "12hrs Ago"))
        self.comboBox.setItemText(6, _translate("Form", "24hrs Ago"))
        self.comboBox.setItemText(7, _translate("Form", "48hrs Ago"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Search Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = filter_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
