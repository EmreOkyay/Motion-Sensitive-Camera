from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 40, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 320, 141, 61))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 130, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 220, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setWhatsThis("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 320, 141, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your email"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter reciever email"))
        self.pushButton_2.setText(_translate("MainWindow", "Continue"))

    def pop_up_1(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Gmail section left empty!")
        pop.exec_()
    def pop_up_2(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Password section left empty!")
        pop.exec_()
    def pop_up_3(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Reciever section left empty!")
        pop.exec_()
    def pop_up_4(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Gmail and Password section left empty!")
        pop.exec_()
    def pop_up_5(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Gmail and Receiever section left empty!")
        pop.exec_()
    def pop_up_6(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Password and Reciever section left empty!")
        pop.exec_()
    def pop_up_7(self):
        pop = QMessageBox()
        pop.setWindowTitle("Error!")
        pop.setText("Gmail, Password and Reciever section left empty!")
        pop.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
