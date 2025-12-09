# Import socket module
import socket

clint_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clint_socket.connect(("127.0.0.1",12345)) # connect to server

print("Server connected.")
clint_socket.close()
print("Client socket closed.")
