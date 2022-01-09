from protos import helloworld_pb2_grpc, helloworld_pb2


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("GreeterServicer.Sayhello() was called !")
        return helloworld_pb2.HelloReply(
            message=f"hello {request.name}"
        )
