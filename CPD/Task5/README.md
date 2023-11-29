# Разобрать пример Python с GitHub.

## В github пример Python. С добавленным сервисом и полями, которые используются. ##
### Добавлено удаление продукта через gRPC ###
## Листинг кода ##
1. ### client.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-29 11:04:44 am
 # @copyright SMTU
 #
import grpc
import product_info_pb2
import product_info_pb2_grpc
import time;

def run():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = product_info_pb2_grpc.ProductInfoStub(channel)

    response = stub.addProduct(product_info_pb2.Product(name = "Apple iPhone 11", description = "Meet Apple iPhone 11. All-new dual-camera system with Ultra Wide and Night mode.", price = 699.0 ))
    print("add product: response", response)
    productInfo = stub.getProduct(product_info_pb2.ProductID(value = response.value))
    print("get product: response", productInfo)
    resp_2 = stub.addProduct(product_info_pb2.Product(name = "Apple iPhone X", description = "Meet Apple iPhone X. All-new dual-camera system with Ultra Wide and Night mode.", price = 699.0 ))
    deletedProduct = stub.deleteProduct(product_info_pb2.ProductID(value = resp_2.value))
    print("delete product: responce", deletedProduct)
run()
```
2. ### server.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-29 11:04:39 am
 # @copyright SMTU
 #
from concurrent import futures
import logging
import uuid
import grpc
import time

import product_info_pb2
import product_info_pb2_grpc

class ProductInfoServicer(product_info_pb2_grpc.ProductInfoServicer):

    def __init__(self):
        self.productMap = {}

    def addProduct(self, request, context):
        id = uuid.uuid1()
        request.id = str(id)
        print("addProduct:request", request)
        self.productMap[str(id)] = request
        response = product_info_pb2.ProductID(value = str(id))

        print("addProduct:response", response)
        return response

    def getProduct(self, request, context):
        print("getProduct:request", request)
        id = request.value
        response = self.productMap[str(id)]
        print("getProduct:response", response)
        return response
    def deleteProduct(self, request, context):
        print("deleteProduct:request", request)
        id = request.value
        responce = self.productMap.pop(str(id))
        print("deleteProduct:responce", responce)
        return responce


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
product_info_pb2_grpc.add_ProductInfoServicer_to_server(
        ProductInfoServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
```
3. ### product_info.proto ###
```cpp
syntax = "proto3";

package ecommerce;

service ProductInfo {
    rpc addProduct(Product) returns (ProductID);
    rpc getProduct(ProductID) returns (Product);
    rpc deleteProduct(ProductID) returns (Product);
}

message Product {
    string id = 1;
    string name = 2;
    string description = 3;
    float price = 4;
}

message ProductID {
    string value = 1;
}
```
## Результат работы ##

<image src="images/pht.png" alt="Рисунок 1 - Результат работы программы">