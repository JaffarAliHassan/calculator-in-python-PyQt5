from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from main_ui import Ui_Form

class Main(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.edit_Ui()
        self.pushButton_13.clicked.connect(lambda: self.click(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.click(self.pushButton_14))
        self.pushButton_15.clicked.connect(lambda: self.click(self.pushButton_15))
        self.pushButton_16.clicked.connect(lambda: self.click(self.pushButton_16))
        self.pushButton_17.clicked.connect(lambda: self.click(self.pushButton_17))
        self.pushButton_18.clicked.connect(lambda: self.click(self.pushButton_18))
        self.pushButton_19.clicked.connect(lambda: self.click(self.pushButton_19))
        self.pushButton_20.clicked.connect(lambda: self.click(self.pushButton_20))
        self.pushButton_21.clicked.connect(lambda: self.click(self.pushButton_21))
        self.pushButton_22.clicked.connect(lambda: self.click(self.pushButton_22))
        self.pushButton_24.clicked.connect(lambda: self.click(self.pushButton_24))

        self.pushButton_5.clicked.connect(lambda: self.opreater("/"))
        self.pushButton_6.clicked.connect(lambda: self.opreater("*"))
        self.pushButton_7.clicked.connect(lambda: self.click(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.click(self.pushButton_8))
        self.pushButton_9.clicked.connect(self.resulte)

        self.pushButton_2.clicked.connect(self.Delete)
        self.pushButton_3.clicked.connect(self.Delete)
        self.pushButton_4.clicked.connect(self.Delete2)

    def edit_Ui(self):
        self.setWindowTitle("calculator")

    def click(self, s):
        self.lineEdit.setText(self.lineEdit.text() + s.text())

    def opreater(self, s):
        self.lineEdit.setText(self.lineEdit.text() + s)

    def resulte(self):
        self.text = self.lineEdit.text()
        self.TheResulte = eval(self.text)
        self.lineEdit.setText(str(self.TheResulte))

    def Delete(self):
        self.lineEdit.setText("")

    def Delete2(self):
        self.lineEdit.backspace()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()