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
import sys
import signal
import time
import logging
_LOGGER = logging.getLogger(__name__)


def run():
    #Коннектимся к серверу и получаем от него канал связи для grpc
    channel = grpc.insecure_channel('localhost:50051')

    #Передаем его в качестве аргумента в конструктовр protobuf-сервиса и получаем его объект
    stub = order_management_pb2_grpc.OrderManagementStub(channel)
    #Создаем объект заказа 
    order1 = order_management_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],
                                        price=2450.50,
                                        description='[delay] This is a Sample order - 1 : description.', 
                                        destination='San Jose, CA')

    #Получаем заказ с сервера по idslee
    try:
        order = stub.getOrder(order_management_pb2.Order(id='0'))
        _LOGGER.info("Call success: %s", order.id)
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Call error: %s",  rpc_error)


    #print("Order service response", order)

    # Unary RPC : Adding an Order
    #Добавляем заказ в список заказов
    response = stub.addOrder(order1, timeout = 3)
    #print('Add order response :', response)

    # Server Streaming
    # Получаем поток объектов, которые соответсвуют поиску
    #for order_search_result in stub.searchOrders(wrappers_pb2.StringValue(value='Item - A')):
        #print('Search Result : ', order_search_result)

    # Client Streaming
    # Обновляем список заказов, предавая поток заказов
    upd_order_iterator = generate_orders_for_updates()
    upd_status = stub.updateOrders(upd_order_iterator)
    #print('Order update status : ', upd_status)


    # Bi-di Streaming 
    # На основе bi-di стриминга сервер читает данные из клиентского потока и записывает в него свои ответы
    proc_order_iterator = generate_orders_for_processing()
    def cancel_request(unused_signum, unused_frame):
        proc_order_iterator.cancel()
        sys.exit(0)
    signal.signal(signal.SIGINT, cancel_request)
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