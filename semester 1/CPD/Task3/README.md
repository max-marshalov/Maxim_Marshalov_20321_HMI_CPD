###TCP Client-streaming (Клиент, например, раз в 1 секунду отправляет данные на сервер), используя встроенный в Python модуль socket.###

1. Task_3_1_server.py Task_3_1_client.py Используя encode() и decode()
1.1 Листинг server.py
    *##
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
            print(data.decode("utf-8"))*
1.2 Листинг client.py
*##
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
        socket.send(data.encode("utf-8"))*
<image src="images/first.png" alt="Рисунок 1 - Результат работы программы">
2. Task_3_2_server.py Task_3_2_client.py Используя pickle - де/сериализация произвольных объектов.
2.1 Листинг server.py
*##
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
            print(data['data'])*
2.2 Листинг client.py
*##
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
        socket.send(send_data)*
<image src="images/second.png" alt="Рисунок 2 - Результат работы программы">
3. Task_3_3_server.py Task_3_3_client.py Используя Google Protocol Buffers - де/сериализация определенных структурированных данных, а не произвольных объектов Python
3.1 Листинг server.py
*##
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
            *
3.2 Листинг client.py
*##
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
data.msg = "Hello world"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        time.sleep(1)
        send_data = data.SerializeToString()
        socket.send(send_data)
        print(send_data)* 
<image src="images/third.png" alt="Рисунок 3 - Результат работы программы">
