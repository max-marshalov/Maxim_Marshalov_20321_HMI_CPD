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
        send_frame = msg.SerializeToString()
        socket.sendall(struct.pack("H", len(send_frame)) + send_frame)
        print(len(send_frame))
        cv2.imshow('client', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 