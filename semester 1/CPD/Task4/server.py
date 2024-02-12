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
import struct
import cv2
from PIL import Image
import numpy as np
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
        
        data = bytes()
        payload_size = struct.calcsize("q") 
        while len(data) < payload_size:
            data += self.clientConnection.readAll().data()
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += self.clientConnection.readAll().data()
        frame_data = data[:msg_size]
        data = data[msg_size:]
        self.serialize_data = frame_data
        print(len(self.serialize_data))
        self.show_data()
    def show_data(self):
            self.msg.ParseFromString(self.serialize_data)
            a = self.msg.frame
            
            img = cv2.imdecode(np.frombuffer(a, np.uint8), cv2.IMREAD_COLOR)
            #rgb_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            resized_up = cv2.resize(img, (self.msg.width, self.msg.hight), interpolation= cv2.INTER_LANCZOS4)
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
        
            sharpened_image = cv2.filter2D(resized_up, -1, kernel) 
            
            _, frame = cv2.imencode(".jpg", sharpened_image)
            picture = QPixmap()
            picture.loadFromData(frame.tobytes())
            self.main_window.image.setPixmap(picture)
            self.serialize_data = bytes()