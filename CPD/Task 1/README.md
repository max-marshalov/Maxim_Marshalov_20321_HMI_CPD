## Task_5_1_Interceptors
- Server-Side Interceptors
### Листинг кода
``` py
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
```
### Результат работы
<image src="images/interceptor.png" alt="img">

## Task_5_2_Deadlines
### Листинг кода
#### client.py
```py 
order1 = order_management_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],
                                        price=2450.50,
                                        description='[delay] This is a Sample order - 1 : description.', 
                                        destination='San Jose, CA')
response = stub.addOrder(order1, timeout = 3)
```
#### server.py
```
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
```
### Результат работы
<image src="images/deadline.png" alt="img">

## Task_5_3_Cancellation

### Листинг кода
```py
proc_order_iterator = generate_orders_for_processing()
    def cancel_request(unused_signum, unused_frame):
        proc_order_iterator.cancel()
        sys.exit(0)
    signal.signal(signal.SIGINT, cancel_request)
    for shipment in stub.processOrders(proc_order_iterator):
        print(shipment)
```

## Task_5_4_Error_Handling
### Листинг кода
#### client.py
```py
 try:
        order = stub.getOrder(order_management_pb2.Order(id='0'))
        _LOGGER.info("Call success: %s", order.id)
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Call error: %s",  rpc_error)
```
### server.py
```py
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
```
### Результат работы
<image src="images/handling.png" alt="img">