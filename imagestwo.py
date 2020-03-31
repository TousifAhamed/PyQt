# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagestwo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# Objective of project is to show images whenever user is clicking on buttons
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 791, 381))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("somewhere.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.somewhere = QtWidgets.QPushButton(self.centralwidget)
        self.somewhere.setGeometry(QtCore.QRect(60, 440, 75, 23))
        self.somewhere.setObjectName("somewhere")
        self.tousiftemple = QtWidgets.QPushButton(self.centralwidget)
        self.tousiftemple.setGeometry(QtCore.QRect(570, 450, 75, 23))
        self.tousiftemple.setObjectName("tousiftemple")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.somewhere.clicked.connect(self.show_somewhere)
        self.tousiftemple.clicked.connect(self.show_tousiftemple)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.somewhere.setText(_translate("MainWindow", "somewhere"))
        self.tousiftemple.setText(_translate("MainWindow", "tousiftemple"))

    def show_somewhere(self):
        self.photo.setPixmap(QtGui.QPixmap("somewhere.jpg"))
    
    def show_tousiftemple(self):
        self.photo.setPixmap(QtGui.QPixmap("tousiftemple.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
