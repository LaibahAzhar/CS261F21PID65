from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_Form
import sys,resource  
import csv
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())






# In[ ]:




