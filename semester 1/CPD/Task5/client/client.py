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