##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-01 12:23:50 pm
 # @copyright SMTU
 #
import cv2
import time
from typing import Optional
import PySide6.QtGui
from server import VideoServer
from PySide6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QLabel, QHeaderView, QTableWidgetItem, QMenu
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
import sys
PORT = 8080
SIZEOF_UINT16 = 2
class MainWindowController(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        self.setWindowTitle("Server")
        self.server = VideoServer(self, PORT)
        self.image = QLabel()
        self.image.setText("Some Text")
        self.setCentralWidget(self.image)
        self.image.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowController()
    window.show()
    sys.exit(app.exec())