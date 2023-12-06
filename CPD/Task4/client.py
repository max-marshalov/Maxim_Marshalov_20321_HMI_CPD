##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-01 2:07:56 pm
 # @copyright SMTU
 #
import socket
import cv2 
import time
import video_msg_pb2
import struct
vid = cv2.VideoCapture(0)
import numpy as np
HOST = 'localhost'
PORT = 8080
msg = video_msg_pb2.VideoMessage()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        r, frame = vid.read()
        height, width, _ = frame.shape
        compressed_frame = cv2.resize(frame, (176, 144), interpolation=cv2.INTER_AREA)
        # g_compressed_frame = cv2.cvtColor(compressed_frame, cv2.COLOR_BGR2GRAY)
        r, buf = cv2.imencode(".jpg", compressed_frame)
        msg.frame = buf.tobytes()
        msg.hight = height
        msg.width = width
        msg.id = len(buf.tobytes())
        send_frame = msg.SerializeToString()
        socket.sendall(struct.pack("q", len(send_frame)) + send_frame)
        print(len(send_frame))
        cv2.imshow('client', frame)
       
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 