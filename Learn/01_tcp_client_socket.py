# TCP Socket Programming Example
# Import the socket module
import socket

# Import Sys module for system-specific parameters and functions
import sys

try:
    # Create a TCP/IP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print(f"Socket creation failed with error {err}")
    sys.exit()

# Define the server address and port
server_address = input("Enter server address (e.g., 127.0.0.1 or www.example.com): ")
server_port = int(input("Enter server port (e.g., 8080): "))

# Connect the socket to the server
try:
    tcp_socket.connect((server_address, server_port))
    print(f"Successfully connected to {server_address} on port {server_port}") 
    tcp_socket.shutdown(2)
except socket.error as err:
    print(f"Connection to {server_address} on port {server_port} failed with error {err}")
    sys.exit()


