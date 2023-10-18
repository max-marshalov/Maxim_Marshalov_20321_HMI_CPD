##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 10:41:21 am
 # @copyright SMTU
 #
import socket
import pickle
import time
HOST = 'localhost'
PORT = 8080
data = {'data': "Hello world",
        'type': ("character string", b"byte string")
        }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        time.sleep(1)
        send_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
        socket.send(send_data)