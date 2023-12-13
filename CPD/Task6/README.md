# Разобрать пример Python с GitHub c вашими комментариями.
## Листинг кода ##
1. ### client.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-12-06 12:27:06 pm
 # @copyright SMTU
 #
from google.protobuf import wrappers_pb2
import grpc
import order_management_pb2
import order_management_pb2_grpc

import time


def run():
    #Коннектимся к серверу и получаем от него канал связи для grpc
    channel = grpc.insecure_channel('localhost:50051')


    #Передаем его в качестве аргумента в конструктовр protobuf-сервиса и получаем его объект
    stub = order_management_pb2_grpc.OrderManagementStub(channel)
    #Создаем объект заказа 
    order1 = order_management_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],
                                        price=2450.50,
                                        description='This is a Sample order - 1 : description.', 
                                        destination='San Jose, CA')

    #Получаем заказ с сервера по id
    order = stub.getOrder(order_management_pb2.Order(id='101'))
    print("Order service response", order)

    # Unary RPC : Adding an Order
    #Добавляем заказ в список заказов
    response = stub.addOrder(order1)
    print('Add order response :', response)

    # Server Streaming
    # Получаем поток объектов, которые соответсвуют поиску
    for order_search_result in stub.searchOrders(wrappers_pb2.StringValue(value='Item - A')):
        print('Search Result : ', order_search_result)

    # Client Streaming
    # Обновляем список заказов, предавая поток заказов
    upd_order_iterator = generate_orders_for_updates()
    upd_status = stub.updateOrders(upd_order_iterator)
    print('Order update status : ', upd_status)


    # Bi-di Streaming 
    # На основе bi-di стриминга сервер читает данные из клиентского потока и записывает в него свои ответы
    proc_order_iterator = generate_orders_for_processing()
    for shipment in stub.processOrders(proc_order_iterator):
        print(shipment)


def generate_orders_for_updates():
    '''Создаем 3 объекта заказа и заполняем ими список\n
    Функция вернет генератор'''
    ord1 = order_management_pb2.Order(id='101', price=1000, 
                                      items=['Item - A', 'Item - B', 'Item - C', 'Item - D'], 
                                      description='Sample order description.', 
                                      destination='Mountain View, CA')
    ord2 = order_management_pb2.Order(id='102', price=1000, 
                                      items=['Item - E', 'Item - Q', 'Item - R', 'Item - D'], 
                                      description='Sample order description.', 
                                      destination='San Jose, CA')
    ord3 = order_management_pb2.Order(id='103', price=1000, 
                                      items=['Item - A', 'Item - K'], 
                                      description='Sample order description.', 
                                      destination='San Francisco, CA')
    list = []
    list.append(ord1)
    list.append(ord2)
    list.append(ord3)

    for updated_orders in list:
        yield updated_orders

def generate_orders_for_processing():
    '''Создаем 3 объекта заказа и заполняем ими список\n
    Функция вернет генератор'''
    ord1 = order_management_pb2.Order(
        id='104', price=2332,
        items=['Item - A', 'Item - B'],  
        description='Updated desc', 
        destination='San Jose, CA')
    ord2 = order_management_pb2.Order(
        id='105', price=3000, 
        description='Updated desc', 
        destination='San Francisco, CA')
    ord3 = order_management_pb2.Order(
        id='106', price=2560, 
        description='Updated desc', 
        destination='San Francisco, CA')
    ord4 = order_management_pb2.Order(
        id='107', price=2560, 
        description='Updated desc', 
        destination='Mountain View, CA')
    list = []
    list.append(ord1)
    list.append(ord1)
    list.append(ord3)
    list.append(ord4)

    for processing_orders in list:
        yield processing_orders

run()
```
2. ### server.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-12-06 12:27:33 pm
 # @copyright SMTU
 #
from concurrent import futures
import time
from typing import OrderedDict
import uuid
from google.protobuf import wrappers_pb2

import grpc
import order_management_pb2_grpc
import order_management_pb2

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer): 

    def __init__(self):
        self.orderDict = {}
        #Заполняем словарь заказов какими-то данными
        self.orderDict['101'] = order_management_pb2.Order(id='101', price=1000, 
                                                           items=['Item - A', 'Item - B'], 
                                                           description='Sample order description.')
        self.orderDict['102'] = order_management_pb2.Order(id='102', price=1000, 
                                                           items=['Item - C'], 
                                                           description='Sample order description.')
        self.orderDict['103'] = order_management_pb2.Order(id='103', price=1000, 
                                                           items=['Item - A', 'Item - E'], 
                                                           description='Sample order description.')
        self.orderDict['104'] = order_management_pb2.Order(id='104', price=1000, 
                                                           items=['Item - F', 'Item - G'], 
                                                           description='Sample order description.')                                                           

    # Метод для получения заказов
    #Основан на стандартном удаленном вызове, берет значение из словаря по ключу
    def getOrder(self, request, context):
        order = self.orderDict.get(request.value)
        if order is not None: 
            return order
        else: 
            # Error handling 
            print('Order not found ' + request.value)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order : ', request.value, ' Not Found.')
            return order_management_pb2.Order()

    # Метод добавления заказа
    #Основан на стандартном удаленном вызове, добавляет значение в словарь по ключу
    def addOrder(self, request, context):
        id = uuid.uuid1()
        request.id = str(id)
        self.orderDict[request.id] = request
        response = wrappers_pb2.StringValue(value=str(id))
        print(self.orderDict)
        return response

    # Метод поиска
    #Основан на принципе сервер-стриминга, searchInventory пробегается по словарю и ищет вхождение и возвращает список предполагаемых объектов
    # Функция  пробегается по нему и возвращает их в виде генераторов
    def searchOrders(self, request, context):  
        matching_orders = self.searchInventory(request.value)
        for order in matching_orders:
            yield order
    
    # Метод обновления заказов
    # Основан на принципе клиент-стриминга, клиент передает на сервер поток объектов,
    # Сервер пробегается по потоку , ищет значение в словаре заказов и обновляет данные
    def updateOrders(self, request_iterator, context):
        response = 'Updated IDs :'
        for order in request_iterator:
            self.orderDict[order.id] = order
            response += ' ' + order.id
        return wrappers_pb2.StringValue(value=response)


    #Метод отдает заказы в обработку
    # Основан на принципе bi-di стриминга, то есть сервер получает поток данных и записывает данные в этом же потоке в структуру CombinedShipment
    # И возвращает генератор этих же объектов обратно, в этом же потоке
    def processOrders(self, request_iterator, context):
        print('Processing orders.. ')
        shipment_id = uuid.uuid1() 
        shipments = []

        shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', )
        shipments.append(shipment)
        for order_id in request_iterator:
            for order in shipments:
                yield order

    # Функция поиска
    def searchInventory(self, query):
        matchingOrders = []    
        for order_id, order in self.orderDict.items(): 
            for itm in order.items:
                if query in itm:
                    matchingOrders.append(order)
                    break
        return matchingOrders
 

# Creating gRPC Server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
```