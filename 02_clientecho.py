import socket as sock

# Define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port number

# Create a socket
client_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send and receive messages
message = input("Enter message: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()