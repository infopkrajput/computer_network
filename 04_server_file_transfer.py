import socket
import os

HOST = '127.0.0.1'
PORT = 12345

# Specify desired receive folder here
SAVE_DIR = "D:/Received_Files" 

# Create the directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")
conn, addr = server_socket.accept()

# 1. Receive filename and strip path info
raw_filename = conn.recv(1024).decode()
filename = os.path.basename(raw_filename) # Extract 'test.txt' from 'C:/path/test.txt'
filepath = os.path.join(SAVE_DIR, filename)

print(f"Receiving: {filename} -> Saving to: {filepath}")

# 2. Receive data in chunks
with open(filepath, 'wb') as file:
    while True:
        data = conn.recv(4096) # Larger buffer for efficiency
        if not data:
            break
        file.write(data)

print("File transfer complete.")
conn.close()
server_socket.close()