# Task_4 Клиент отправляет видео на PySide6 сервер, где проиходит отображение этого видео в виджете. PySide6 server - QTcpServer
## Листинг кода ##
1. ### client.py ##
```python
        ##
        # @author Maxim Marshalov <marshalmaxim@gmail.com>
        # @file Description
        # @desc Created on 2023-11-01 11:59:14 am
        # @copyright SMTU
        #
        import socket
        import cv2 
        import time
        import video_msg_pb2
        vid = cv2.VideoCapture(0)
        HOST = 'localhost'
        PORT = 8080
        msg = video_msg_pb2.VideoMessage()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
            socket.connect((HOST, PORT))
            while True:
                r, frame = vid.read()
                r, buf = cv2.imencode(".jpg", frame)
                msg.frame = buf.tobytes()
                msg.id = len(buf.tobytes())
                # time.sleep(2)
                send_frame = msg.SerializeToString()
                socket.send(send_frame)
                print(len(send_frame))
                cv2.imshow('client', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break

        vid.release()  Destroy all the windows 
        cv2.destroyAllWindows() 
```
2. ### server.py ###
```python
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
```
2. ## Результат работы ##
<image src="images/photo.png" alt="Рисунок 3 - Результат работы программы">