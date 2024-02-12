##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 11:26:22 am
 # @copyright SMTU
 #
import socket
import proto_example_pb2
HOST = ''
PORT = 8080
data = proto_example_pb2.Message()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen(1)
    conn, addr = socket.accept()
    with conn:
        print("Connected")
        while True:
            recv_data = conn.recv(1024)
            data.ParseFromString(recv_data)
            print(data.msg)
            