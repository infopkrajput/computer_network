import socket

# Define server address and port
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message to send
message = "Hello, UDP Server!"

# Send message to server
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

# Receive response from server
data, server_address = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

# Close the socket
#client_socket.close()