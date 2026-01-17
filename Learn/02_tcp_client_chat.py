import socket
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
except socket.error as err:
    print(f"Connection to {server_address} on port {server_port} failed with error {err}")
    sys.exit()

def chat():
    print("You can start chatting now. Type 'exit' to quit.")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Exiting chat...")
            break
        try:
            tcp_socket.sendall(message.encode())
            data = tcp_socket.recv(1024)
            print(f"Server: {data.decode()}")
        except socket.error as err:
            print(f"Error during communication: {err}")
            break
chat()
# Close the socket
tcp_socket.close() 