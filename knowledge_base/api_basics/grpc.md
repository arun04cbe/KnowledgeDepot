# GRPC

1. Used for inter-service communications similar to REST API
2. RPC - Remote Procedure Call
3. Used for communication between distributed systems which uses protocol buffers as interface description language

## What does this do?

1. The data transfer between client and server is very small when compared to REST which uses JSON format
2. Uses HTTP/2
3. REST focuses on working with entities(CRUD), while GRPC is mainly used for communication between services
4. The API contracts is defined using `proto` files, which enforces `encapsulation`.
5. Every services that follows the `proto` files must implement the functionality based on this so there is always a single place of truth.
6. Data is transferred in the form of binary.

## Difference between REST and gRPC

| Functionality |               REST                |          gRPC           |
| :------------ | :-------------------------------: | :---------------------: |
| HTTP version  |             HTTP 1.1              |         HTTP 2          |
| APIs          | Defined using HTTP verbs with URL | Defined using functions |
| Data Format   |               JSON                |         Binary          |

## Important Concepts

1. Protocol buffers have the contracts for the RPC calls.
2. All the fields in `proto3` are strongly typed and are Optional. If any value is unset during an RPC call, it will default to zero for int and empty strings for string type.
3. With the help of the proto file, gRPC will be able to generate a code.
4. Using Python, we will be able to generate client-proxy for gRPC clients to interact with RPC server.
5. This proxy is called `stub`, by which we can talk to the server by just making function calls.
6. The standard port for gRPC is `50051` in the local host.

## Supported Communication Types

1. Unary
2. Server-Streaming
3. Client-Streaming
4. Bi-directional Streaming

An example of gRPC server and client implementation can be seen [here](..\..\code_snippets\test_server_grpc\README.md)
