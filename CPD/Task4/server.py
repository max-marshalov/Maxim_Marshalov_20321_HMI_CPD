##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-01 11:59:14 am
 # @copyright SMTU
 #
import sys
from typing import Optional
from PySide6.QtCore import *
import PySide6.QtCore 
import logging
from PySide6.QtGui import *
from PySide6.QtNetwork import *
from PySide6.QtWidgets import *
import video_msg_pb2


class VideoServer():
    def __init__(self, obj, port):
        self.tcpServer = QTcpServer()
        self.socket = QTcpSocket()
        self.full_data = QByteArray()
        self.serialize_data = bytes()

        self.main_window = obj
        self.msg = video_msg_pb2.VideoMessage()
        if not self.tcpServer.listen(port=port):
            print("Unable to start the server: %s." % self.tcpServer.errorString())
        self.tcpServer.newConnection.connect(self.newConnection)
        
    
    def newConnection(self):
         self.clientConnection = self.tcpServer.nextPendingConnection()
         self.clientConnection.readyRead.connect(self.readData)

    def readData(self):
        data = self.clientConnection.readAll().data()
        self.serialize_data = data
        self.show_data()
    def show_data(self):
            self.msg.ParseFromString(self.serialize_data)
            print(len(self.serialize_data))
            print(len(self.msg.frame))
            picture = QPixmap()
            picture.loadFromData(self.msg.frame)
            self.main_window.image.setPixmap(picture)
            self.serialize_data = bytes()