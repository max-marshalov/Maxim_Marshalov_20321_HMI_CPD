##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 10:41:18 am
 # @copyright SMTU
 #
import socket
import pickle
HOST = ''
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen(1)
    conn, addr = socket.accept()
    with conn:
        print("Connected")
        while True:
            recv_data = conn.recv(1024)
            data = pickle.loads(recv_data)
            print(data['data'])