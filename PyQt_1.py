from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Tech with Tousif")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button You pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the buttonYou pressed the button")
        self.update()
        
    def update(self):
        self.label.adjustSize()


# def clicked():
#     print("Clicked")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())

window()