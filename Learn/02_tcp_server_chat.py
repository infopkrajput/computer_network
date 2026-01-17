import socket
import sys
import threading

try:
    # Create a TCP/IP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print(f"Socket creation failed with error {err}")
    sys.exit()

# Define the server address and port
server_address = '127.0.0.1'
server_port = 12345

# Bind the socket to the address and port
try:
    tcp_socket.bind((server_address, server_port))
    print(f"Socket successfully bound to {server_address} on port {server_port}")
except socket.error as err:
    print(f"Binding to {server_address} on port {server_port} failed with error {err}")
    sys.exit()

# Listen for incoming connections
tcp_socket.listen(5)
while True:
    print("Server is listening for incoming connections...")
    client_socket, client_address = tcp_socket.accept()
    print(f"Connection established with {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed by {client_address}")
                break

            print(f"Client {client_address}: {data.decode()}")
            
            message = input("You: ")
            client_socket.sendall(message.encode())
        except socket.error as err:
            print(f"Error during communication with {client_address}: {err}")
            break
    client_socket.close()
# Close the server socket
tcp_socket.close()