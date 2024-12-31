from src import greet_pb2_grpc, greet_pb2


class GreeterService(greet_pb2_grpc.GreeterServicer):
    """Greeter service implementation."""

    def SayHello(self, request, context):
        """
        Say hello to the user.

        Args:
            request: The request object.
            context: The context object.
        """
        response_message = f"Hello, {request.name}!"
        return greet_pb2.HelloReply(message=response_message)
