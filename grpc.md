# GRPC

1. Used for inter-service communications similar to REST API
2. RPC - Remote Procedure Call
3. Used for communication between distributed systems which uses protocol buffers are interface description language

## What does this do?

1. The data transfer between client and server is very small when compared to REST which uses JSON format
2. Uses HTTP/2
3. REST focuses on working with entities(CRUD), while GRPC is mainly used for communication between services
4. The API contracts is defined using `proto` files, which enforces `encapsulation`.
5. Every services that follows the `proto` files must implement the functionality based on this so there is always a single place of truth.
6. Data is transferred in the form of binary.
