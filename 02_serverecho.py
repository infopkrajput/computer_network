import socket as sock

# Define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port number

# Create a socket
server_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)  # Echo back the received data

    conn.close()