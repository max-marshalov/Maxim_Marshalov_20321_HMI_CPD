##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 10:34:36 am
 # @copyright SMTU
 #
import socket
import time
HOST = 'localhost'
PORT = 8080
data = "Hello world!"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        time.sleep(1)
        socket.send(data.encode("utf-8"))