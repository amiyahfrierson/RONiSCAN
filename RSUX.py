import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QFont, QFontDatabase

import qtawesome as qta


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("RONiSCAN")

        self.setMinimumSize(1920,1080)

        RonFont = QFontDatabase.addApplicationFont("D:\SCHOOL STUFF\RSUX\Poppins-Medium.ttf")
        if RonFont < 0:
            print('font not loaded')

        fontGrab = QFontDatabase.applicationFontFamilies(RonFont)
        

        header = QHBoxLayout()
        footer = QHBoxLayout()
        layout = QGridLayout()
        holder = QVBoxLayout()


        blueToothButton = QPushButton("Bluetooth Scanner")
        carWhisperButton = QPushButton("Car Whisperer Attack")
        mitmButton = QPushButton("Man-in-the-Middle \nAttack")
        deAuthButton = QPushButton("DeAuth Attack")

        blueToothButton.setFont(QFont(fontGrab[0], 70))
        carWhisperButton.setFont(QFont(fontGrab[0], 70))
        mitmButton.setFont(QFont(fontGrab[0], 70))
        deAuthButton.setFont(QFont(fontGrab[0], 70))


        blueToothButton.setFixedSize(800,330)
        carWhisperButton.setFixedSize(800,330)
        mitmButton.setFixedSize(800,330)
        deAuthButton.setFixedSize(800,330)

        homeButton = QPushButton("Home")
        settingsButton = QPushButton("Settings")

        header.addWidget(homeButton)
        header.addWidget(settingsButton)

        homeButton.setFont(QFont(fontGrab[0], 70))
        settingsButton.setFont(QFont(fontGrab[0], 70))

        holder.addLayout(header)
        holder.addLayout(layout)
        holder.addLayout(footer)


        layout.addWidget(blueToothButton, 0, 0)
        layout.addWidget(carWhisperButton, 0, 1)
        layout.addWidget(mitmButton, 1, 1)
        layout.addWidget(deAuthButton, 1, 0)

        widget = QWidget()
        widget.setLayout(holder)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

style = """
    QWidget{
        color: #fff;
        font-size: 50px;
        background: #1C221E;
    }

    QPushButton{
        color: #fff;
        font-size: 70px;
        background: #343B37
    }
"""

app.setStyleSheet(style)
window = MainWindow()
window.show() 

app.exec()
