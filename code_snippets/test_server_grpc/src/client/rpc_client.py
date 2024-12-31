import grpc
from src import greet_pb2_grpc, greet_pb2


def run():
    # Connect to the server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        # Make a request to the SayHello method
        response = stub.SayHello(greet_pb2.HelloRequest(name="Arun"))
        print("Server response:", response.message)


if __name__ == "__main__":
    run()
