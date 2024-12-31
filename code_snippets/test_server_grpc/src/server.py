import grpc
from src import greet_pb2_grpc
from src.services.greeter_service import GreeterService
from concurrent import futures


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the service to the server
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)

    # Bind the server to a port
    server.add_insecure_port("[::]:50051")
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
