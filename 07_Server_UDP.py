import socket

# Define server address and port
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"UDP server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    # Receive data from client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode()}")

    # Send response back to client
    server_socket.sendto(b"Message received!", client_address)