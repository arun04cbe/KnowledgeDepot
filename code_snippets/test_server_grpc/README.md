# GRPC server and client implementation using Python

## How did the grpc_pb2.py and grpc_pb2_grpc.py files were created?

python -m grpc_tools.protoc -I <path in which the proto file is present> --python_out=<path to store the generated file> --grpc_python_out=<path to store the generated file> <proto file path>

## What are the generated files?

### grpc_pb2

1. Contains the serialization logics for the grpc message transfer.
2. All the message types are all defined in the `.proto` file will be present as data classes.

### grpc_pb2_grpc

1. Contains the base class for the server
2. Contains the stub class for the client-interactions

Once you start the application, the server will be running in the `localhost:50051`.
