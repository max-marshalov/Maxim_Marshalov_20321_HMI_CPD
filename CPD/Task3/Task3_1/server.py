##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-18 10:34:39 am
 # @copyright SMTU
 #
import socket

HOST = ''
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen(1)
    conn, addr = socket.accept()
    with conn:
        print("Connected")
        while True:
            data = conn.recv(1024)
            print(data.decode("utf-8"))