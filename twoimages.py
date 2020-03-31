# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twoimages.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# Objective of this project is 

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_photo(object):
    def setupUi(self, MainWindow):
        photo.setObjectName("MainWindow")
        photo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 771, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tousifatbgm.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tousifatbgm = QtWidgets.QPushButton(self.centralwidget)
        self.tousifatbgm.setGeometry(QtCore.QRect(0, 490, 321, 61))
        self.tousifatbgm.setObjectName("tousifatbgm")
        self.somewhere = QtWidgets.QPushButton(self.centralwidget)
        self.somewhere.setGeometry(QtCore.QRect(500, 490, 291, 61))
        self.somewhere.setObjectName("somewhere")
        photo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(photo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        photo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        photo.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tousifatbgm.clicked.connect(self.show_tousif_at_temple)
        self.somewhere.clicked.connect(self.show_somewhere)

    def retranslateUi(self, photo):
        _translate = QtCore.QCoreApplication.translate
        photo.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tousifatbgm.setText(_translate("MainWindow", "Tousif @ BGM"))
        self.somewhere.setText(_translate("MainWindow", "Somewhere else"))

    def show_tousif_at_temple(self):
        self.photo.setPixmap(QtGui.QPixMap("tousifatbgm.jpg"))
    
    def show_somewhere(self):
        self.photo.setPixmap(QtGui.QPixmap("somewhere.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    photo = QtWidgets.QMainWindow()
    ui = Ui_photo()
    ui.setupUi(photo)
    photo.show()
    sys.exit(app.exec_())
