##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-29 11:04:39 am
 # @copyright SMTU
 #
from concurrent import futures
import time
from typing import OrderedDict
import uuid
from google.protobuf import wrappers_pb2
from concurrent import futures
import grpc
import time
import asyncio
import contextvars
import logging
from typing import Awaitable, Callable, Optional
import order_management_pb2
import order_management_pb2_grpc
import datetime
from google.rpc import code_pb2
from google.rpc import error_details_pb2
from google.rpc import status_pb2
from grpc_status import rpc_status

from google.protobuf import any_pb2
rpc_id_var = contextvars.ContextVar("rpc_id", default="default")

class RPCProdInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self, tag: str, rpc_id: Optional[str] = None) -> None:
        self.tag = tag
        self.rpc_id = rpc_id
    async def intercept_service(
        self,
        continuation: Callable[
            [grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]
        ],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler:
        """
        This interceptor prepends its tag to the rpc_id.
        If two of these interceptors are chained together, the resulting rpc_id
        will be something like this: Interceptor2-Interceptor1-RPC_ID.
        """
        data = dict(handler_call_details.invocation_metadata)
        logging.info(f"{handler_call_details.method}, {data['user-agent']}, {datetime.datetime.now()}")
        
            
        logging.info("%s called with rpc_id: %s", self.tag, rpc_id_var.get())

        return await continuation(handler_call_details)
    
    def decorate(self, rpc_id: str, method_name, time):
        return f"{self.tag}-{rpc_id}"
   

class ProductInfoServicer(order_management_pb2_grpc.OrderManagementServicer):

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
    def not_found_error_status(self, name):
        detail = any_pb2.Any()
        return status_pb2.Status(
            code=code_pb2.INVALID_ARGUMENT,
            message="Not found",
            details=[detail],
        )
   
    def getOrder(self, request, context):
        order = self.orderDict.get(request.value)
        if order is not None: 
            return order
        else: 
            # Error handling 
            rich_status = self.not_found_error_status(request.value)
            context.abort(rpc_status.to_status(rich_status).code, rpc_status.to_status(rich_status).details)

    # Метод добавления заказа
    #Основан на стандартном удаленном вызове, добавляет значение в словарь по ключу
    def addOrder(self, request, context):
        msg = request.description
        if msg.startswith('[delay]'):
            time.sleep(5)
        id = uuid.uuid1()
        request.id = str(id)
        self.orderDict[request.id] = request
        response = wrappers_pb2.StringValue(value=str(id))
        #print(self.orderDict)
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
        #print('Processing orders.. ')
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

async def serve():
    
    inters = [RPCProdInterceptor("Logging inter")]

    # create a gRPC server
    server = grpc.aio.server(interceptors=inters)

    # use the generated function `add_CalculatorServicer_to_server`
    # to add the defined class to the server
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(
            ProductInfoServicer(), server)
# listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

# since server.start() will not block,
# a sleep-loop is added to keep alive
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
