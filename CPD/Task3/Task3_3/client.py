##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 11:26:19 am
 # @copyright SMTU
 #
import socket
import time
import proto_example_pb2
HOST = 'localhost'
PORT = 8080
data = proto_example_pb2.Message()
data.msg = "Hello proto"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        time.sleep(1)
        send_data = data.SerializeToString()
        socket.send(send_data)
        print(send_data)